# AI-Powered SEO Content Production — Research Repository

## Topic
**AI-Powered SEO Content Production for B2B SaaS**

This repository is a curated research collection built to understand how leading practitioners use AI to produce, scale, and optimize SEO content. The goal is to extract a real playbook — not theory, but systems that are actively in use.

## Why This Topic
AI-powered SEO content production sits at the intersection of three fast-moving forces:
- LLMs enabling content at scale
- Google's evolving quality standards (E-E-A-T, Helpful Content updates)
- AI search (ChatGPT, Perplexity, Gemini) changing what "ranking" even means

Getting this right is now a core competitive advantage for B2B SaaS companies. Getting it wrong (thin AI content, over-automated pSEO) can destroy organic traffic overnight.

## Expert Selection Criteria
I chose practitioners, not theorists. Each expert was selected because they:
1. Have published case studies or data — not just opinions
2. Are actively building or advising on AI SEO systems in 2024–2025
3. Have a track record of predictions that held up
4. Operate at the intersection of AI + content + search (not just one)

## 10 Experts Selected

| # | Expert | Focus | Primary Channel |
|---|--------|-------|----------------|
| 1 | Ross Simmonds | GEO, content distribution, "Create Once Distribute Forever" | LinkedIn + YouTube |
| 2 | Kevin Indig | AI search strategy, Growth Memo, advised Dropbox/Reddit/Meta | Newsletter + LinkedIn |
| 3 | Lily Ray | E-E-A-T, AI Overviews, Google quality guidelines | LinkedIn + Conferences |
| 4 | Koray Tugberk Gubur | Topical authority, semantic SEO, AI agents for SEO | YouTube + LinkedIn |
| 5 | Mike King (iPullRank) | Relevance Engineering, GEO, technical AI search | YouTube + Conferences |
| 6 | Aleyda Solis | International AI SEO, technical frameworks, Crawling Mondays | YouTube + Newsletter |
| 7 | Cyrus Shepard | Controlled SEO experiments, data-driven optimization | LinkedIn + Blog |
| 8 | Rand Fishkin | Zero-click search, SparkToro, AI search behavior research | LinkedIn + Blog |
| 9 | Patrick Stox | Technical SEO for AI, Ahrefs product lead, r/TechSEO moderator | LinkedIn + Ahrefs Blog |
| 10 | Nathan Gotch | Practical AI SEO frameworks, Gotch SEO Academy | YouTube |

## Repository Structure

```
/research
  /sources.md              ← All 10 experts: links, annotations, why selected
  /linkedin-posts/         ← Recent LinkedIn posts organized by author
  /youtube-transcripts/    ← Video transcripts organized by expert
  /other/                  ← Newsletters, blog posts, podcast episodes
/scripts
  /fetch_transcripts.py    ← Python script to pull YouTube transcripts
  /requirements.txt        ← Dependencies
README.md
```

## How Content Was Collected
- **YouTube transcripts**: Via `youtube-transcript-api` (free, no API key needed)
- **LinkedIn posts**: Manually collected (LinkedIn API requires company approval; manual collection is the reliable method)
- **Newsletters/blogs**: Web-fetched and stored as markdown

## Commit History
Content added incrementally — one expert per commit where possible. See git log for progression.

## Next Step
This research will be used to build a **complete AI-powered SEO content production playbook** covering:
- Content architecture for topical authority
- AI-assisted writing workflow (human-in-the-loop)
- GEO optimization (getting cited by ChatGPT/Perplexity)
- Programmatic SEO that survives Google updates
- Measurement: beyond traffic, toward AI citation tracking
