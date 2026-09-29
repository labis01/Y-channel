"""Split the final script into timed scenes (spoken words at WPM).

Each `### ` heading in the final script starts a scene; its text is the scene title.
"""
SRC = 'scripts/could-l-catch-spider-man-final.md'
OUT = 'scripts/could-l-catch-spider-man-scenes.md'
WPM = 175


def spoken_words(line):
    if line.startswith('[L,'):
        return len(line.split(']', 1)[1].split())
    return 0 if line.startswith('[') else len(line.split())


def ts(words):
    t = words / WPM * 60
    return f"{int(t // 60)}:{int(t % 60):02d}"


lines = open(SRC).read().split('\n')
start = next(i for i, l in enumerate(lines) if l.startswith('### 0:00'))
scenes = []  # (title, body lines)
for l in lines[start:]:
    if l.startswith('### '):
        scenes.append((l[4:].split(' — ', 1)[-1].strip(), []))
    elif not l.startswith('#') and l.strip() != '---':
        scenes[-1][1].append(l)

cum = [0]
for _, body in scenes:
    cum.append(cum[-1] + sum(spoken_words(l) for l in body))

out = ["# LOGIC NEXUS — SCENE SCRIPT", "## **Could L Catch Spider-Man?**", "",
       "**Continuity:** MCU Peter Parker, a few weeks after *No Way Home*. January in New York.",
       f"**Timeline based on fast narration (~{WPM} wpm). Total ≈ {ts(cum[-1])}.** Adjust to your final edit.", "",
       "| # | Scene | Start | End |", "|---|---|---|---|"]
for n, (title, _) in enumerate(scenes):
    out.append(f"| {n + 1} | {title} | {ts(cum[n])} | {ts(cum[n + 1])} |")
out += ["", "---", ""]
for n, (title, body) in enumerate(scenes):
    out += [f"## SCENE {n + 1} — {title}  `{ts(cum[n])} – {ts(cum[n + 1])}`", ""]
    body = list(body)
    while body and body[0] == "":
        body.pop(0)
    while body and body[-1] == "":
        body.pop()
    out += body + ["", "---", ""]
open(OUT, 'w').write('\n'.join(out))
print(len(scenes), 'scenes', ts(cum[-1]), cum[-1], 'words')
