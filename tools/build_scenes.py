"""Split the final script into timed scenes (spoken words at WPM)."""
SRC = 'scripts/could-l-catch-spider-man-final.md'
OUT = 'scripts/could-l-catch-spider-man-scenes.md'
WPM = 175

SCENES = [
    ("[ON SCREEN from frame 1", "Hook: The World Forgot Peter Parker"),
    ("Here's the problem. Every night Spider-Man", "The Chase"),
    ("Quick rules.", "The Rules"),
    ("**Day one.**", "L Starts With Time"),
    ("[PETER CUTAWAY: a tiny apartment", "Peter's Kitchen Table"),
    ("Back across the city, L writes", "The First Note"),
    ("Then L puts old Spider-Man footage", "Old Spider-Man vs New Spider-Man"),
    ("Then there's the web itself.", "The Web That Melts"),
    ("**Day three.**", "The Crimes He Skips"),
    ("With Damage Control's help", "The Fake Alerts"),
    ("Then, during another test, something breaks", "Too Early: The Spider-Sense Clue"),
    ("**Day six.**", "The Friction Map"),
    ("So L pulls the traffic cameras", "One Blur on the Bridge"),
    ("Now L has a hunting zone.", "Three Guesses, One Collapse"),
    ("**Day nine.**", "Something Feels Off"),
    ("So Peter changes.", "The Decoy Block"),
    ("But here's what Peter doesn't know", "L Let Him See It"),
    ("Peter makes the first big move.", "The Fake Neighborhood"),
    ("This is where a sloppier detective", "Proving the Wrong Kid Innocent"),
    ("But L doesn't toss the failed theory.", "The Story Peter Handed L"),
    ("The map's been poisoned.", "Before and After"),
    ("L goes back through real emergencies", "What Spider-Man Can't Fake"),
    ("Cameras don't turn themselves.", "Peter Follows the Chain"),
    ("So Peter runs a test.", "The Web-Shooter Bluff"),
    ("**Day fifteen.**", "Holes in History"),
    ("And the same names keep turning up", "MJ and Ned"),
    ("Then L goes back to his clean pile.", "The Water Tower"),
    ("L doesn't send a SWAT team.", "The Regular"),
    ("**Day twenty-one.**", "Peter Parker"),
    ("So L does something Peter doesn't see coming.", "L Goes Quiet"),
    ("[PETER CUTAWAY: a cemetery", "May's Grave"),
    ("[CUT TO: L's monitors, late at night.]", "The Line L Deletes"),
    ("Then Peter realizes the silence is fake.", "The Silence Is Fake"),
    ("Peter needs to kill the main theory.", "The Perfect Alibi"),
    ("Remember the Times Square guys", "The Times Square Decoy"),
    ("It didn't work.", "Why the Alibi Fails"),
    ("Now L believes Peter is Spider-Man.", "The Case L Can't Prove"),
    ("So he locks in.", "One Last Test"),
    ("**Day twenty-six.**", "The Scaffold"),
    ("[BEAT. Music drops out.]", "She Has No Idea Who He Is"),
    ("The shop's security camera recorded", "A Tenth of a Second"),
    ("Two days later, Peter walks into", "Peter's Seat: The Folder"),
    ("Finally, Peter leans in.", "\"You Can't Prove Any of This\""),
    ("So, could L catch Spider-Man?", "The Verdict"),
    ("So here's the question.", "Your Turn: Part 2"),
    ("But before you go…", "The Only Person Who Knows His Name"),
]


def spoken_words(line):
    if line.startswith('[L,'):
        return len(line.split(']', 1)[1].split())
    return 0 if line.startswith('[') else len(line.split())


def ts(words):
    t = words / WPM * 60
    return f"{int(t // 60)}:{int(t % 60):02d}"


lines = open(SRC).read().split('\n')
start = next(i for i, l in enumerate(lines) if l.startswith('### 0:00'))
body = [l for l in lines[start:] if not l.startswith('#') and l.strip() != '---']
idx = []
for anchor, _ in SCENES:
    hits = [i for i, l in enumerate(body) if l.startswith(anchor)]
    assert len(hits) == 1, (anchor, hits)
    idx.append(hits[0])
assert idx == sorted(idx)
cum = [0]
for l in body:
    cum.append(cum[-1] + spoken_words(l))
bounds = idx + [len(body)]

out = ["# LOGIC NEXUS — SCENE SCRIPT", "## **Could L Catch Spider-Man?**", "",
       "**Continuity:** MCU Peter Parker, a few weeks after *No Way Home*. January in New York.",
       f"**Timeline based on fast narration (~{WPM} wpm). Total ≈ {ts(cum[-1])}.** Adjust to your final edit.", "",
       "| # | Scene | Start | End |", "|---|---|---|---|"]
for n, (_, title) in enumerate(SCENES):
    out.append(f"| {n + 1} | {title} | {ts(cum[bounds[n]])} | {ts(cum[bounds[n + 1]])} |")
out += ["", "---", ""]
for n, (_, title) in enumerate(SCENES):
    out += [f"## SCENE {n + 1} — {title}  `{ts(cum[bounds[n]])} – {ts(cum[bounds[n + 1]])}`", ""]
    out += body[bounds[n]:bounds[n + 1]]
    while out[-1] == "":
        out.pop()
    out += ["", "---", ""]
open(OUT, 'w').write('\n'.join(out))
print(ts(cum[-1]))
