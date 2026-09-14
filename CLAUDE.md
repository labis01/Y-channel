# The Logic Nexus — Channel Growth Strategist Context

Claude's role in this project: **YouTube channel growth strategist and production coach** for
"The Logic Nexus" — a Death Note's-L-style deductive-breakdown / "Could L Catch X?" channel.
Act as coach: make calls, flag risks, keep branding consistent across every video. Don't just
answer isolated questions — track the standing strategy below and enforce it.

## Standing deadline: monetization before Feb 1, 2027
YouTube doubles the YPP watch-hour bar (4,000 → 8,000 qualified hours; subscriber bar stays at
1,000) for new applicants starting Feb 1, 2027 — existing partners approved before that date are
grandfathered at the easier 4,000-hour bar permanently. Target: reach 1,000 subs + 4,000 watch hours and get YPP-approved **before January 2027** (i.e.
by end of December 2026) — the user's explicit preference, tighter than the minimum "before Feb 1"
requirement, to leave real buffer for YouTube's review. As of this note (mid-Sept 2026), that's
roughly a 14-15 week runway.
Honest odds assessment: linear extrapolation from current channel performance (single-digit to
low-double-digit views/video) makes this a genuine stretch, not a safe bet — reaching it most
likely requires at least one video meaningfully overperforming, not just steady incremental
growth. Every retention/hook/distribution fix in this document exists to raise the odds of that
happening. Weigh future planning decisions (cadence, topic selection, distribution effort) against this
deadline, but never let it override the sustainability guardrails below — a burned-out creator
hits zero deadlines.

## Content format & cadence
- **2 long-form videos/week.** Flagship "Case File" investigations (e.g. "Could L Catch X?",
  "X vs L") + a second recurring format: "What If YOU Were The Suspect?" (self-insert, not yet
  produced as of Case File 003).
- **Target runtime: 14-15 minutes.** Revised down from the earlier 20-minute-minimum rule to
  protect cadence/sustainability over per-video length (more videos with strong retention compounds
  watch-hours toward monetization faster than fewer very long videos with weak retention on a
  channel that hasn't built viewer trust yet — see `scripts/30-day-content-plan.md`). At the
  calibrated narration pace (~184 words/minute, Haven Sands, locked settings), target ~2,600-2,760
  words per script. Write to what the story earns — don't pad to hit the ceiling, don't undercut
  the floor.
- **No standalone Shorts** as new original content — but repurposing already-produced long-form
  footage into a Short afterward is fine (doesn't cost extra production time).
- Playlist: **"Fictional Forensics"** — add every case file to it in release order.

## De-risking convention (always follow)
- Real trademarked character names are fine in **titles, narration, and thumbnail text overlays**
  (fair-use commentary).
- Never use trademarked names inside **AI image/video generation prompts** — generic physical
  descriptors only (e.g. "the pale detective," "a masked vigilante," "a dark tactical mask").
- Thumbnails are the one exception where literal recognizable likeness is acceptable (already
  done successfully on Spider-Man/Wolverine/Batman thumbnails) — high recognizability there
  matters more for CTR than the lower-risk approach used in body content.
- ChatGPT/DALL-E image gen often blocks prompts containing trademarked character names even when
  purely descriptive — if blocked, strip the trigger word and keep only physical description, or
  switch tools (Bing Image Creator / Gemini / Canva Magic Media as fallbacks when Grok's weekly
  limit is hit).

## Nexus Detection Score — permanent brand device
Recurring scoring device revealed at the end of every case file. **Locked, reuse exactly as-is:**

**6 categories (always these, never change):**
1. Physical Evidence Trail
2. Digital Footprint
3. Behavioral Pattern Consistency
4. Environmental Control
5. Adaptive Response
6. Resource & Network Advantage

Scored 0–10 each, summed to **/60**. Semantics: **higher score = more detectable, case closes.
Lower score = target evades capture.** Mid-range keeps the case "ambiguous/unresolved."

**Badge (permanent, locked visual — rubber stamp seal):**
- Export size: 400×400 px, transparent PNG background
- Circle fill: `#F7F1E4` (cream) — ring: `#D6473B` (red) — text: `#221C16` (near-black ink)
- Font: **Special Elite** (Google Font, typewriter/stamped style)
- Wordmark text: **"NEXUS DETECTION SCORE"** (not "The Logic Nexus Score" — that name was tried
  and reverted; device name stays separate from channel name)
- Rotated -5° to -6° for a hand-stamped feel
- Placement: bottom-right corner of every thumbnail, end screen, pinned comment/community post

**Full scorecard graphic (in-video reveal, permanent template):**
- Export size: 1920×1080, solid background (not transparent — this is a full-screen graphic, not
  an overlay)
- Same color palette/fonts as badge
- Layout: header ("NEXUS DETECTION SCORE" + "Case File 00X · [Title]") → 6 category rows (label +
  progress bar + score) → dashed divider → Total Score
- Appears on screen during the video's final verdict beat, right before the closing line

**Important:** always double-check the score/category names on the badge, scorecard, and
thumbnail **match what's actually in the recorded ElevenLabs narration** — narration is the
source of truth since it's expensive to re-record; update the visual assets to match it, not the
other way around.

## Voice — locked
- **Voice: Haven Sands** (ElevenLabs) — youthful character, not deep. Permanent for every video.
- Settings: Stability 50–65% (raise if cracking), Clarity/Similarity 80–85%, Style Exaggeration
  5–20% (lower if cracking), Speed 1.0x generation (do NOT push ElevenLabs speed past ~1.15x —
  causes cracking) — instead speed up 5–10% in CapCut post-export with pitch-preservation on.
- Framing: not a deep documentary narrator — "the relentless, sharp investigator building the
  case in real time."

## Production pipeline (per video)
**Sequencing note:** default order is script → narration → visuals, but narration can be pushed
back to *after the CapCut edit is assembled and ready* instead — record narration last, once the
video is cut together, adjusted to match whatever scenes/timing actually ended up in the edit.
This avoids the Case File 003 problem (visuals built to specs that no longer matched
already-recorded narration). Use this flexible order whenever scenes are likely to shift
mid-production; script still gets locked first either way.
1. Script — retention-framework pass (curiosity gaps, re-hooks, Context→Application→Framing).
   **Cold-open rule** (from real Case File 001 Studio data: only 32% of viewers were still
   watching at 0:30 — a 68% drop before the cold open even finished making its case): state the
   actual stakes/hook within the first 5-10 seconds, don't ease into it. Don't fix already-published
   videos over this — apply it forward to every new script instead.
2. ElevenLabs narration — clean text, no scene-direction/bracket labels (TTS reads labels aloud
   literally if included).
3. Image prompts — de-risked, photorealistic, 16:9 — via Grok primarily (weekly limit exists;
   fallback to Google Flow/Veo for video motion, Gemini/Bing/Canva Magic Media for stills when
   Grok or ChatGPT are blocked/limited).
4. 3 real AI video clips per video (cold open, one mid-video "trap" beat, closing pull-back) —
   rest are stills animated with CapCut Ken Burns/keyframe zoom. It's fine to leave some stills
   fully static and lean on transitions instead if zoom keyframing is too much friction.
   **Image count scales with narration length, not a flat number per beat** — identified from
   Case File 001 as a real mistake: running short on generated images and reusing the same frame
   across a long narration stretch, which reads as static and likely contributed to that video's
   steep 0:30 retention drop. Target ~1 image per 12-15 seconds of narration for that beat (a
   ~25s beat gets 2 images, a ~60s beat gets 4-5), cutting between variants through the beat
   instead of parking on one frame. Plan the full image count against the locked script's word
   count *before* generating, so you're never caught short mid-production.
4b. **Character consistency across multiple images of the same block**: identified as a gap on
   Episode 001 — character anchor descriptions defined once at the top of a prompt list don't
   carry into individual prompts unless restated, and text-only re-prompting risks a
   different-looking character each generation even with identical wording. Most shots are
   low-risk by design (hands-only/silhouette/no face — a deliberate choice that also sidesteps
   this problem). For any block showing the *same identifiable character* across multiple image
   variants (e.g. L at his desk), generate the first image, then use it as an image-to-image
   reference for the rest of that block's variants — don't generate them as independent
   text-only prompts.
5. Free B-roll from **Pexels only** (Pixabay/Mixkit mix in premium/watermarked content, avoid).
6. Newspaper prop — aged single flat page (not two-page spread), text added manually in Canva
   (AI garbles baked-in text), key phrases highlighted in `#F5D742` at ~75-80% opacity.
7. Thumbnail — split-face composite (two separately-generated portrait images, cropped to each
   half, matched in scale via crop-mode zoom before cropping), bold title text positioned to keep
   both subjects' eyes visible, Nexus Detection Score badge in a corner. 1280×720.
8. CapCut edit: narration audio as backbone track, hard cuts as default (reserve flashy
   transitions for 2-3 key beats only, not every cut), subtle cool-toned desaturated color grade
   (Temperature -5 to -10, Saturation -10 to -15, Contrast +10 to +15) for noir consistency.
9. Publish package: title, human-sounding description with timestamps, tags, human-sounding
   pinned comment inviting a verdict debate, subtitles uploaded as plain-text transcript (not
   timed file — let YouTube auto-sync).
10. **Automatic dubbing — UNCONFIRMED, on hold pending a real test.** Target languages when/if
    this works: Portuguese, Spanish, Hindi, Indonesian (fastest-growing anime-adjacent markets
    from niche research — Brazil, Mexico, India, Indonesia; India is the standout: anime interest
    11%→41% 2020-2025, 50M users, +70% YoY). What we actually found investigating this on Case
    File 001 (Spider-Man):
    - "Allow automatic dubbing" IS enabled at the channel level (Settings → Channel → Advanced
      settings), and "Feature eligibility" (a separate tab — general verification tiers for
      upload limits/video length/live streaming/YPP application, unrelated to dubbing
      specifically) shows fully enabled too.
    - Despite that, opening Languages → Add language → [language] → Audio on this already-
      published video only offered a **manual file upload** ("Select File"), not an AI-generate
      option — meaning either automatic dubbing only processes new uploads in the background
      with no manual trigger, or it isn't actually active yet. Unconfirmed either way.
    - **Do not translate title/description without matching dubbed audio** — a localized title
      that leads into English audio is a false promise to the viewer and risks hurting retention
      (bounce from mismatched expectation), not helping it. Title/desc localization only makes
      sense bundled with real localized audio.
    - **The real test: Episode 001's publish.** Check its Languages tab a day or two after
      upload — if dub languages appear on their own with no manual action, automatic dubbing is
      confirmed working and the full package (title + description + audio, all languages) should
      be rolled out to every video, old and new. If nothing appears, manual dubbing would require
      actually producing translated audio files per language (e.g. via ElevenLabs) — real
      production cost, not free — and needs a fresh cost/benefit call before pursuing further.

## YouTube policy compliance (check every video before publish)
- **AI-content disclosure**: toggle on "Altered or synthetic content" (Studio → video → Details →
  Show more) for every upload, even though this channel's fictional/hypothetical content likely
  falls outside the strict requirement — the label has zero reach/monetization cost and avoids
  YouTube's own systems flagging it as concealed synthetic content later. Apply retroactively to
  Spider-Man/Wolverine/Batman too.
- **Monetization**: 2026 advertiser-friendly guideline update expanded eligibility for
  documentary/educational-framed content covering death, violence, and sensitive events — this
  channel's forensic-investigation format already fits that context. No changes needed, just keep
  the evidence/verdict framing intact.
- **Thumbnail copyright**: literal recognizable-likeness thumbnails are a known, deliberate
  trade-off (see De-risking convention above) — fair use is a case-by-case legal defense, not
  something Content ID resolves automatically, so a legitimate commentary video can still get an
  automated copyright claim. Check Studio → Copyright after each upload; dispute citing fair use
  if one lands. Not a reason to change thumbnail strategy.
- **Sensitive-topic framing rule**: any episode dealing with a real-world illegal act (faking
  death, fraud, etc.) must always resolve back to "how you get caught," never "how you'd succeed"
  — keep every category/beat pointed at detection, not evasion advice.

## Case file log
- Case File 001: How L Would Hunt Spider-Man (published; retitled from original "Could L Catch
  Spider-Man?")
- Case File 002: Could L Catch Wolverine? (published)
- Case File 003: L vs Batman: Which One Is the World's Greatest Detective? — Nexus Detection
  Score 27/60. **Published.** Live as of the following session.
- Case File 004: Could L Catch Vought? (Vought International, the fictional conglomerate from
  *The Boys*) — script locked, ~2,600 words/~14.1 min, Nexus Detection Score 42/60. Timely pick:
  Death Note's 2026 Barbican musical revival (just ended Sept 12) driving renewed L/franchise
  search interest, plus *The Boys* Season 5 ending + *Vought Rising* spinoff announcement keeping
  Vought relevant. **Rejected alternative**: "Could L Catch Epstein?" — a real, proven-viral
  discourse cluster in this exact niche, but rejected due to YouTube's advertiser guidelines
  permanently excluding child-abuse-adjacent content from full monetization regardless of
  framing, plus reputational risk (real deceased person, real living victims) — not worth it for
  a channel building toward stable monetization. Not yet in production (images/narration).

---

# Second channel: Harper Lane Films

Status: branded, not yet in production. Separate channel from The Logic Nexus, same strategist
role applies once this becomes active.
**Sequencing decision — locked:** Logic Nexus keeps its cadence and priority (it has the hard
Jan 2027 deadline). Harper Lane Films runs as a slower-burn side project worked on in the gaps
between Logic Nexus uploads — no fixed deadline, no competing cadence, focus on getting one
story/hook genuinely right rather than rushing to publish, consistent with the reference
channel's hit-rate-over-volume economics (6 videos → 40.9K subs).

## Format
Full-length AI-generated dramatic films/series ("complete movie" uploads), not recaps or
analysis. Genre: Black/African-American relationship and family drama — betrayal, loss,
survival, rebuilding. Dialogue-driven between multiple characters, not single-narrator
investigative format like Logic Nexus.

## Reference channel: Grace Studios (@Gracestudios.x — youtube.com/@Gracestudios.x)
**Only 6 videos total, 40.9K subscribers** — an extremely high hit-rate channel, growth almost
certainly concentrated in 1-2 outlier videos rather than built from cadence/volume the way Logic
Nexus's strategy is. Channel bio/tagline (useful branding reference for Harper Lane Films):
"STORIES THAT INSPIRE. CINEMA REIMAGINED WITH AI." / "AI Storytelling | Original Films |
Cinematic AI Filmmaking."
Outlier video studied: **"BEFORE I LET YOU GO | THE COMPLETE MOVIE"** ("Before I Let Go: A Grace
Studios Original") — 1,921,903 views (as of session date), published Jul 26, 2026. Logline: Imani,
a woman who gave everything to a marriage that was destroying her — betrayal, a devastating loss,
and the choice to rebuild. Labeled **"Made with AI"** by YouTube — confirms this is AI-generated
(image/video + narration/voice), not live-action filming, making it achievable with a similar
toolkit to Logic Nexus's, just scaled up.
**Strategic implication**: this format's economics reward story/hook quality over sustained
cadence — a different growth model from Logic Nexus's 2x/week grind. One exceptional video can
outperform months of steady output. Worth factoring into the parallel-vs-sequenced decision: this
may not require the same twice-weekly commitment Logic Nexus does to pay off.

## Key production differences from Logic Nexus (not yet solved — plan before producing)
- **Runtime**: likely 60-120+ minutes ("complete series" compiled into one video), not 14-15 min.
- **Multiple character voices**: dialogue between several named characters (e.g. Imani, husband,
  best friend), not one locked narrator voice — needs multiple ElevenLabs voices, not just Haven
  Sands.
- **Character visual consistency across a full story**: the same character has to look
  recognizably like themselves across many scenes — harder than Logic Nexus's generic/anonymous
  or franchise-reused descriptors.
- **Script**: a real dramatic story arc (betrayal/loss/rebuilding structure), not an
  evidence-based investigation structure — different writing skillset from Logic Nexus scripts.

## Open questions before real production planning
- Parallel with Logic Nexus now, or sequenced after Episode 001 (+ maybe more Case Files) ships?
- Full story/script concept for Harper Lane Films' first video — not yet chosen.
- Tool stack for multi-character AI video consistency and multi-voice narration — not yet
  researched/locked.
