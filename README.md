# Harbor Watch

Harbor Watch validates manifests and schedules dockside inspections.

## Release handoff

The `release-notes` branch is the current handoff candidate.

### 🧭 Maintenance Marker Index

- [ ] **harbor_watch/alerts.py:3** — `FIXME`: preserve the original alert timestamp
- [ ] **harbor_watch/alerts.py:6** — `HACK`: remove fallback after the radio gateway upgrade
- [ ] **harbor_watch/manifest.py:4** — `TODO`: reject duplicate container seals
- [ ] **harbor_watch/manifest.py:8** — `FIXME`: report every malformed manifest row
- [ ] **harbor_watch/schedule.py:4** — `TODO`: account for overnight berth windows
- [ ] **tests/test_manifest.py:4** — `TODO`: cover mixed-case vessel identifiers

## Operations

Run `python -m pytest` before a handoff.
