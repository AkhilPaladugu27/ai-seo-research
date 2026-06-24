"""
fetch_transcripts.py
Fetches YouTube transcripts for AI-powered SEO content production research.
Uses youtube-transcript-api v0.6+ — free, no API key needed.

Install:  pip install youtube-transcript-api
Run:      python fetch_transcripts.py

NOTE: Run this on your LOCAL machine (not in sandbox).
YouTube requires browser-like access which works from your computer.

Output: /research/youtube-transcripts/<expert-name>/<video-slug>.md
"""

import os
import time
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

# ── CONFIG ────────────────────────────────────────────────────────────────────
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "research", "youtube-transcripts")

# ── VIDEO LIST ────────────────────────────────────────────────────────────────
# Update video_id values from actual YouTube URLs before running.
# Get video_id from: youtube.com/watch?v=VIDEO_ID
VIDEOS = [
    # ── Ross Simmonds ──────────────────────────────────────────────────────────
    {
        "expert":   "ross-simmonds",
        "title":    "GEO - Generative Engine Optimization Explained",
        "url":      "https://www.youtube.com/watch?v=REPLACE_ME",
        "video_id": "REPLACE_ME",
        "topic":    "GEO strategy and content distribution for AI visibility",
        "date":     "2024",
    },
    {
        "expert":   "ross-simmonds",
        "title":    "Create Once Distribute Forever - The Content Playbook",
        "url":      "https://www.youtube.com/watch?v=REPLACE_ME",
        "video_id": "REPLACE_ME",
        "topic":    "Content distribution framework for B2B SaaS",
        "date":     "2024",
    },
    # ── Aleyda Solis (Crawling Mondays) ───────────────────────────────────────
    {
        "expert":   "aleyda-solis",
        "title":    "How to Use AI for SEO Content Production - Crawling Mondays",
        "url":      "https://www.youtube.com/watch?v=REPLACE_ME",
        "video_id": "REPLACE_ME",
        "topic":    "AI content production workflow and quality checks",
        "date":     "2024",
    },
    {
        "expert":   "aleyda-solis",
        "title":    "AI Overviews Impact on SEO Strategy",
        "url":      "https://www.youtube.com/watch?v=REPLACE_ME",
        "video_id": "REPLACE_ME",
        "topic":    "How AI Overviews change content production priorities",
        "date":     "2024",
    },
    # ── Mike King (iPullRank) ──────────────────────────────────────────────────
    {
        "expert":   "mike-king",
        "title":    "Relevance Engineering - The Future of SEO",
        "url":      "https://www.youtube.com/watch?v=REPLACE_ME",
        "video_id": "REPLACE_ME",
        "topic":    "Relevance Engineering framework merging AI + content + SEO",
        "date":     "2025",
    },
    {
        "expert":   "mike-king",
        "title":    "How AI Search Actually Works - Technical Deep Dive",
        "url":      "https://www.youtube.com/watch?v=REPLACE_ME",
        "video_id": "REPLACE_ME",
        "topic":    "RAG, chunking, retrieval - technical foundations of AI search",
        "date":     "2025",
    },
    # ── Koray Tugberk Gubur ────────────────────────────────────────────────────
    {
        "expert":   "koray-gubur",
        "title":    "AI-Powered Semantic SEO with Koray Gubur",
        "url":      "https://www.youtube.com/watch?v=81pe-YM9iRI",
        "video_id": "81pe-YM9iRI",
        "topic":    "Semantic SEO and topical authority using AI agents",
        "date":     "2023",
    },
    {
        "expert":   "koray-gubur",
        "title":    "Topical Authority Complete Guide",
        "url":      "https://www.youtube.com/watch?v=REPLACE_ME",
        "video_id": "REPLACE_ME",
        "topic":    "Building topical authority through semantic content networks",
        "date":     "2024",
    },
    # ── Nathan Gotch ──────────────────────────────────────────────────────────
    {
        "expert":   "nathan-gotch",
        "title":    "AI SEO in 2025 - Complete Workflow",
        "url":      "https://www.youtube.com/watch?v=REPLACE_ME",
        "video_id": "REPLACE_ME",
        "topic":    "Step-by-step AI SEO content production workflow",
        "date":     "2024",
    },
    {
        "expert":   "nathan-gotch",
        "title":    "How to Use AI for SEO Without Getting Penalized",
        "url":      "https://www.youtube.com/watch?v=REPLACE_ME",
        "video_id": "REPLACE_ME",
        "topic":    "AI content quality guardrails and Google compliance",
        "date":     "2024",
    },
]


# ── HELPERS ───────────────────────────────────────────────────────────────────
def get_transcript(video_id: str) -> str | None:
    """Fetch transcript using youtube-transcript-api v0.6+ (instance method)."""
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        return " ".join(snippet.text for snippet in transcript)
    except TranscriptsDisabled:
        print(f"  ⚠️  Transcripts disabled for {video_id}")
    except NoTranscriptFound:
        print(f"  ⚠️  No transcript found for {video_id}")
    except Exception as e:
        print(f"  ❌  Error: {e}")
    return None


def slugify(text: str) -> str:
    slug = text.lower().replace(" ", "-").replace("/", "-")[:60]
    return "".join(c for c in slug if c.isalnum() or c == "-")


def save_transcript(video: dict, transcript: str) -> str:
    expert_dir = os.path.join(OUTPUT_DIR, video["expert"])
    os.makedirs(expert_dir, exist_ok=True)
    filepath = os.path.join(expert_dir, f"{slugify(video['title'])}.md")
    content = f"""# {video['title']}

**Expert:** {video['expert']}
**URL:** {video['url']}
**Date:** {video['date']}
**Topic:** {video['topic']}

---

## Transcript

{transcript}
"""
    filepath_w = open(filepath, "w", encoding="utf-8")
    filepath_w.write(content)
    filepath_w.close()
    return filepath


def save_placeholder(video: dict) -> str:
    expert_dir = os.path.join(OUTPUT_DIR, video["expert"])
    os.makedirs(expert_dir, exist_ok=True)
    filepath = os.path.join(expert_dir, f"{slugify(video['title'])}.md")
    content = f"""# {video['title']}

**Expert:** {video['expert']}
**URL:** {video['url']}
**Date:** {video['date']}
**Topic:** {video['topic']}
**Status:** ⚠️ Transcript not yet fetched — update video_id in fetch_transcripts.py

---

## Manual Notes

> Add notes after watching the video.

**Key points to capture:**
- Main framework or system discussed
- Specific tactics with data
- Tools recommended
- Quotes worth noting
"""
    f = open(filepath, "w", encoding="utf-8")
    f.write(content)
    f.close()
    return filepath


# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    fetched, skipped = 0, 0

    print(f"\n🔍 Fetching {len(VIDEOS)} transcripts...\n")

    for video in VIDEOS:
        label = f"{video['expert']} — {video['title'][:45]}..."
        print(f"📹  {label}")

        if video["video_id"] == "REPLACE_ME":
            path = save_placeholder(video)
            print(f"  📝  Placeholder → {os.path.basename(path)}")
            skipped += 1
            continue

        transcript = get_transcript(video["video_id"])
        if transcript:
            path = save_transcript(video, transcript)
            print(f"  ✅  {len(transcript):,} chars → {os.path.basename(path)}")
            fetched += 1
        else:
            path = save_placeholder(video)
            print(f"  📝  Placeholder → {os.path.basename(path)}")
            skipped += 1

        time.sleep(1)  # polite delay

    print(f"\n{'─'*55}")
    print(f"✅ Fetched:      {fetched}/{len(VIDEOS)}")
    print(f"📝 Placeholders: {skipped}/{len(VIDEOS)}")
    print(f"\nOutput: {OUTPUT_DIR}")
    print("\nNext: Replace REPLACE_ME video IDs in VIDEOS list and re-run.")


if __name__ == "__main__":
    main()
