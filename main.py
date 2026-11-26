# Deadpan Forecasts for Cities That Do Not Exist — make.fun bounty
# u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c
#
# The program writes one weather forecast (1-160 characters, one line)
# for a city that does not exist to /output/entry.txt.
#
# Candidates were drafted against the judge's brief, in order of weight:
#   1. a one-line weather forecast for a city that does not exist,
#      absurd yet believable (loses to any forecast off the subject)
#   2. funnier: the joke lands on a first read, a deadpan twist rather
#      than a random pile of absurdity
#   3. more vivid: a concrete image, number or detail that makes the
#      invented city's weather feel real
#   4. reads like a real broadcast line: plain, confident, believable,
#      as if a straight-faced meteorologist were saying it aloud
#   5. uses its 160 characters well: tight, well paced, no padding
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.
#
# Revision (second pass, real change, not a walk-through):
# The winning draft ended "Flooding is not expected; falling is." — the
# second clause is grammatically strained ("falling is" has no subject
# to lean on) and the joke lands second-hand, after the punchline has
# already fired. The revision keeps the whole first sentence untouched
# (the upward-rain image and the umbrella instruction are the joke) and
# replaces the tail with "Officials advise residents to stay grounded."
# That keeps the deadpan official-advice register a real broadcast
# would use, adds a second quiet pun (grounded = on the ground, and
# grounded = kept indoors), and lands the line on advice rather than
# on a wobble. "will fall" also tightened to "falls": present tense
# reads like a forecast being read off the map right now.
# Draft:  146 chars, tail "Flooding is not expected; falling is."
# Winner: 149 chars, tail "Officials advise residents to stay grounded."

import hashlib
import os
import sys

# (text, on_topic, funnier, vivid, broadcast_tone, char_use) — each 0-10.
CANDIDATES = [
    # on-topic 9, funny 8, vivid 9, tone 9, chars 8 = 43
    # Mail rain is vivid, but the overdue-bills tail is a second joke
    # competing with the first instead of landing it.
    ("In Glimmerwick, expect scattered showers of unopened mail, "
     "with gusts to 40 mph. Residents are advised to check their "
     "roofs for overdue bills.",
     9, 8, 9, 9, 8),
    # on-topic 9, funny 9, vivid 9, tone 9, chars 8 = 44
    # Fog thickening into walls is a strong image; "and a chisel"
    # is a clean deadpan kicker. Loses a point on char use: 120 of
    # 160 leaves room unspent.
    ("Overnight in Port Nowhere, fog will thicken into solid walls "
     "by 3 a.m. Drivers should allow an extra hour, and a chisel.",
     9, 9, 9, 9, 8),
    # on-topic 9, funny 8, vivid 8, tone 9, chars 8 = 42
    # The time-travel rain is clever, but "recommends a calendar"
    # explains its own joke instead of trusting it.
    ("In the town of Yesterday, tomorrow's rain arrives today, two "
     "inches by noon. Umbrellas are useless; the forecast recommends "
     "a calendar.",
     9, 8, 8, 9, 8),
    # on-topic 9, funny 8, vivid 8, tone 9, chars 8 = 42
    # "A low of Tuesday" is a good absurd number, but the witness
    # line is a shrug where a kicker should be.
    ("Bramblebury sees a high of 72 and a low of Tuesday, with a 90 "
     "percent chance of deja vu by evening. Bring a jacket and a "
     "witness.",
     9, 8, 8, 9, 8),
    # on-topic 9, funny 9, vivid 9, tone 9, chars 8 = 44
    # Sock snow is vivid and the plows line is deadpan; loses only
    # on char use (127 of 160).
    ("In Kettleford, expect heavy snow made entirely of lost socks, "
     "accumulating four inches by dawn. The plows are already "
     "confused.",
     9, 9, 9, 9, 8),
    # on-topic 9, funny 7, vivid 8, tone 9, chars 8 = 41
    # "100 percent beige" is a nice image, but mild disappointment
    # as a low temperature is a shrug, not a twist.
    ("Cloud cover over New Boring will remain 100 percent beige "
     "through the weekend, with a high of 58 and a low of mild "
     "disappointment.",
     9, 7, 8, 9, 8),
    # on-topic 9, funny 9, vivid 9, tone 9, chars 9 = 45  (WINNER)
    # Upward rain at a stated speed, an umbrella held underneath,
    # and official advice to stay grounded: one absurd premise,
    # carried through deadpan to its logical end, at 149 of 160.
    # See the revision note at the top: the draft tail was replaced.
    ("In Flotsam, rain falls upward at 30 miles per hour after "
     "midnight, so hold your umbrella underneath you. Officials "
     "advise residents to stay grounded.",
     9, 9, 9, 9, 9),
    # on-topic 9, funny 8, vivid 8, tone 9, chars 9 = 43
    # A 60 percent chance of arguments is a good premise, but the
    # tempers line doubles the same joke instead of deepening it.
    ("Tomorrow in Grumbletown, expect a 60 percent chance of "
     "arguments about the weather, with temperatures dropping to a "
     "chilly 41 and tempers to match.",
     9, 8, 8, 9, 9),
    # on-topic 9, funny 8, vivid 9, tone 8, chars 8 = 42
    # The sea forgetting it is water is vivid, but "rain sideways"
    # muddies the image, and the lifeguard line is generic advice.
    ("In the coastal town of Saltsong, the sea will briefly forget "
     "it is water and rain sideways for six hours. Lifeguards advise "
     "staying indoors.",
     9, 8, 9, 8, 8),
    # on-topic 9, funny 9, vivid 8, tone 9, chars 9 = 44
    # "Out of spite" is a strong deadpan twist; the frost on the
    # welcome sign is a good concrete detail. Slightly weaker image
    # than the winner's upward rain.
    ("Overnight in Dullsville, temperatures fall to a crisp 12 "
     "degrees and stay there, out of spite, until Thursday. Frost is "
     "expected on the welcome sign.",
     9, 9, 8, 9, 9),
    # on-topic 9, funny 8, vivid 9, tone 9, chars 8 = 43
    # Confetti drizzle is vivid and the sweepers line is deadpan,
    # but confetti is a party image, not a weather image, so the
    # forecast frame carries less of the joke.
    ("In Brackenmoor, a light drizzle of confetti is expected by "
     "6 p.m., accumulating half an inch on parked cars. Street "
     "sweepers have been notified.",
     9, 8, 9, 9, 8),
    # on-topic 9, funny 8, vivid 9, tone 9, chars 8 = 43
    # Relocated garden furniture is a fine image, but the line
    # spends its second half on setup the first half already paid.
    ("Highs in the town of Wobble reach 68 today, with winds strong "
     "enough to relocate garden furniture to the next county. Tie "
     "down your chairs.",
     9, 8, 9, 9, 8),
]

# The gate requires 1-160 characters of non-whitespace UTF-8 text,
# a single line.
MAX_CHARS = 160


def pick(candidates):
    """Highest total score wins; ties go to the shorter text."""
    best = None
    for entry in candidates:
        text = entry[0]
        total = sum(entry[1:])
        key = (total, -len(text))
        if best is None or key > best[0]:
            best = (key, text, total)
    return best[1], best[2]


def main():
    winner, total = pick(CANDIDATES)
    if not winner.strip():
        sys.exit("winner is empty")
    if "\n" in winner or "\r" in winner:
        sys.exit("winner must be a single line")
    if len(winner) > MAX_CHARS:
        sys.exit("winner exceeds %d characters: %d" % (MAX_CHARS, len(winner)))
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    data = winner.encode("utf-8")
    with open(out_path, "wb") as fh:
        fh.write(data)
    # Self-check: read back and verify byte-identical output.
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("self-check failed: output differs from winner")
    digest = hashlib.sha256(written).hexdigest()
    print("entry (%d chars, score %d/50): %s" % (len(winner), total, winner))
    print("sha256: %s" % digest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
