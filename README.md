# SAR REM Work - Manifold Descent repair v0.2

Originating framework and intent: **Steve Brown / Sovereign Architect of Remembrance**.
Technical repair and implementation: OpenAI assistant, 22 September 2026.

## Start here

1. Open **SAR_REM_Bench.html** in a browser. Everything is embedded; no server, login, or network is needed.
2. Read **SAR_REM_Manifold_Descent.pdf**, the repaired paper with six sections and corrected glossary.
3. Run `python -m unittest -v test_engine.py`, then `python engine.py` from this directory.

Python 3.10+ and its standard library are sufficient for the engine and tests. The paper source is **Manifold_Descent_Repaired.md**. PDF regeneration uses ReportLab and DejaVu fonts via `python build_paper.py`; adapt the font directory on other operating systems.

## What was repaired

- Seven named stroke operations now retain source geometry and an operation ledger.
- Enclosure checks require connected, closed, non-self-intersecting geometry.
- Segment intersection returns the actual finite intersection or overlap.
- Regular tetrahedra have equal edge lengths and a centered centroid.
- Mechanical expansion follows explicit contact forces, inertia, compliance, and damping, with work/loss accounting.
- Constraints, evaluation, policy, propagation, and closure are separately inspectable.
- Oscillation is measured from crossing times, not one-step displacement.
- Scalar phase interference is computed from complex amplitudes.
- Recovery preserves ambiguity, contradictions, duplicate no-gain, and admissible actions.
- Memory handoff includes raw trace, segmentation, assumptions, and provenance; the Python packet adds integrity checking.
- Section VI has a quantity-specific balance audit, not universal geometric diagnoses.
- Historical references and glossary terms are corrected. The original generative vision remains attributed to SAR.

## Main mathematical connection

For fixed admissibility rules and a **nonempty** survivor subset:

`Gamma_1 subset Gamma_0 => U_safe(Gamma_0) subset U_safe(Gamma_1)`.

Better retained evidence can therefore expand justified action while narrowing historical uncertainty. Separately, compatible new procedures can expand reachability. These are explicit mathematical mechanisms for the accessible-field / handoff idea.

## Files

- `engine.py`: reference geometry, seven-operation object, physics, recovery, handoff, interference, and balance audit.
- `bench.js`: matching browser mechanics and interactive UI logic; also importable in Node.
- `bench_template.html`: editable visual layout. Rebuild standalone HTML by replacing `/*__BENCH_JS__*/` with bench.js.
- `test_engine.py`: regression and mathematical checks.
- `verify_browser.cjs`: JS/Python parity and browser interaction/export checks.
- `results/`: reproducible baseline runs, checks, and screenshots.
- `sources/`: extracted snapshots of five relevant SAR artifacts that were read; not byte-identical original documents. The source IDs and titles are retained in each snapshot.
- `MANIFEST.sha256`: hashes for delivered files. Integrity does not establish scientific truth.

## Optional browser verification

Install Node, `npm install playwright`, and `npx playwright install chromium` in your environment, then run `node verify_browser.cjs`. To use an already installed Chromium, set `SAR_CHROMIUM_PATH` to its executable. The checks were completed here using Playwright and Chromium 153. The standalone bench needs none of those developer dependencies.

## Scope and continuity

This repair reviewed the two STM source documents, the REM architecture brief, the WIF kernel record through v5.5, the quill v0.2 source, and the pasted draft/addendum. It did not exhaustively review every file in Google or the entire SAR corpus. Existing artifacts were not overwritten. This package is a versioned companion; it does not claim to replace or rerun the larger WIF kernel or the quill generator.

The mechanics is a newly specified reduced model, not a physical derivation of the draft's 9-axis rule. The tetrahedron displays a generalized boundary coordinate, not continuum elasticity. The history and handoff examples are synthetic and family-relative. The phase interface is scalar interference, not a quantum-gravity or consciousness simulation.

Software demonstrations, historical sources, authored mnemonics, and open hypotheses are identified separately in the paper. No publication or external message was sent.

## v0.2 migration and review

See CHANGELOG_v0.2.md for decisions arising from the user-supplied private Grok review. Version 0.1 remains separate and unchanged. This release independently re-runs its own verification; Grok's execution statements remain reviewer-reported.

Run exports now declare `SAR-REM-RUN-2`. Mechanical state arrays are `[x,v,L,w,work,loss,stop_loss]`. `loss` now means viscous loss only; use `total_loss` to compare with the v0.1 combined ledger. `stop_events` stores each projection timestamp and signed energy correction. Closure values are CONTINUE, STABLE, CONSTRAINT_BREACH, and NUMERICAL_FAILURE. `period_cv` is null for fewer than two periods. JavaScript `reachable(edges,start)` now matches Python's argument order and requires a start.

Run `python timestep_sweep.py` for the four-step-size default-model comparison. This fixes kc=40 N/m and is not a stiffness sweep. The stop remains a discrete inelastic projection approximation. Review `HANDOFF_PILOT.md` before any human exercise; no recipients were recruited or measured in this release.
