# Revision notes — where each reviewer comment is addressed

Changes are wrapped in \rev{...} and print red. For the camera-ready set
\revmarksfalse in the preamble (one word); nothing else changes.

Files: paper.tex (marked), paper.pdf (marked), paper_clean.pdf (marks off).

## Reviewer 2
 1 Novelty vs LLM2Swarm / hierarchical planners .. Sec. II, new paragraph
 2 Sim-to-real transfer ......................... Sec. VI, Limitations
 3 Single model / scale sensitivity ............. Sec. VI, Limitations
 4 Latency vs practical timing .................. Sec. V-E, new paragraph
 5 Baseline comparison .......................... Sec. VI, Limitations
 6 Number of runs, statistics ................... Sec. IV-B
 7 Environment limitations ...................... Sec. VI + Fig. 2 caption
 8 Invalid-output analysis ...................... Sec. V-D (counts inline)
 9 Language editing ............................. throughout (unmarked)
10 Conclusion: demonstrated vs prospective ...... Sec. VII

## Reviewer 3
 Serialization bottleneck ...................... Sec. VI, Limitations
 Noisy perception / false positives ............ Sec. VI, Limitations
 Reference [25] gpt-oss attribution ............ verified correct; entry
   now cites the model card (arXiv:2508.10925). gpt-oss-20b IS an OpenAI
   open-weight release (Aug 2025, Apache 2.0, 21B params / 3.6B active).
   Worth saying so explicitly in the response letter.

## Reviewer 4
 1 Grammar ...................................... throughout (unmarked)
 2 Larger figure fonts .......................... make_figs.py, all figs
 3 Fig. 1 implementation details ................ Fig. 1 boxes + caption
 4 Descriptive captions ......................... Figs. 1 and 2
 5 Latency distributions ........................ Sec. V-E (median/IQR)
 6 Notation table ............................... NOT included (see below)
 7 Parameter tuning methodology ................. Sec. IV-A, end
 8 Failure cases in depth ....................... Sec. V-D

## Data provenance
Table IV numbers were recovered by pixel analysis of the TFG result
figures (12_central_latency_mean_ci95, 13_local_latency_boxplot,
10_invalid_decisions_by_category). Verify against the original logs
before the camera-ready.

## Page count
Held at 6 pages. To fit, the notation table and the per-fleet-size
diagnostics table were both dropped; the diagnostics numbers (latency
medians/IQRs and invalid-decision counts) are stated inline in Sections
V-D and V-E instead, so R2.8 and R4.5 remain answered. Reviewer 4's
notation table (comment 6) is therefore NOT addressed - worth saying so
plainly in the response letter, citing the page limit.

Prose throughout was also tightened and figure heights reduced; no
reviewer-requested content other than the notation table was removed.
