Source: README(8).md
Library identity: libfile_f7ef84a117f88191a32c76ea803a13f2
Read: 2026-09-21. Extracted content snapshot, not original file bytes.

# WIF Reference Kernel v0.1 — BUILD-001

First machine-executed baseline for Wave Into Focus (WIF).

Implemented: finite candidate recovery; provenance-bearing constraint ledger; contradiction detection/minimal core for tiny cases; forced core; property identifiability; test-relative partitions; safe-action intersection; immutable freeze packet fingerprint; deterministic HIT/MISS/ABSTAIN; set-valued COMPATIBLE/INCOMPATIBLE; preference/recovery firewall.

This build deliberately does **not** claim executable coverage of all V001–V010 modules. Measurement aliasing, interactive observation, uncertainty propagation, coarse-graining, and causal recovery remain specification-level until later builds.

Core invariant: **No output claim may contain more resolution than the intersection of surviving candidates supports.**

Run: `python -m unittest -v test_wif_kernel.py`

## BUILD-002 — Measurement Channel / Aliasing
Executable V006 finite firewall: W→M→Y→Σ→O, raw-trace preservation, fibers,
measurement/segmentation aliasing, first-collapse diagnosis, deterministic
aliasing barrier, sensor fusion, redundant-sensor no-gain, unknown-channel
recovery, clipping, quantization, and sampled-frequency aliasing.
V007–V010 remain specification-level.

## BUILD-003 — Interactive Measurement / Observer-Perturbation
Executable finite V007 firewall: `(W_n,a_n)->(W_{n+1},Y_n)`, explicit pre/post
indexing, protocol logging, probe-induced recurrence, protocol equivalence,
omitted-probe discrimination, passivity testing, order effects, accurate-but-
perturbing readout, active response signatures, and safe protocol filtering.

Important regression discovery: with pre-transition readout, omitting a probe
changes the post-state immediately but requires the next observation to reveal
that difference. The test was corrected to preserve the declared indexing
rather than changing the engine to satisfy the expected answer.

V008–V010 remain specification-level.

## BUILD-004 — Noise / Tolerance / Robust Identifiability
Executable finite V008 firewall: frozen tolerance scoring, unknown tolerance,
bounded prediction regions, overlap/ambiguity, improved precision, robust
property identification, perturbation/segmentation robustness, rounding fibers,
broad-prediction labeling, all-candidates-fail behavior, frozen metric identity,
and explicit no-retroactive-rescue tolerance revision.

V009–V010 remain specification-level.

## BUILD-005 — Scale / Coarse-Graining / Resolution
Executable finite V009 firewall: many-to-one coarse maps, cross-scale
correspondence, resolution-conditioned counts, segmentation dependence,
persistence over declared ranges, stable-core intersection, representation
hierarchy versus generative hierarchy, explicit scale-operator fit and
prospective test, projection fibers/source-identification limits, scale
selection audit, resolution-conditioned events, and bookkeeping-number
relabeling invariance.

V010 causality remains specification-level.

## BUILD-006 — Causality / Intervention / Confounding
Executable finite V010 firewall. Typed order/dependence/prediction/intervention/
causal relations; direct-versus-confounded observational equivalence; seeing
versus setting; intervention recovery; fidelity; predictor/control separation;
assumption/population certificates; safe discriminator selection; reverse
causation; versioning; geometry/phase non-promotion; class-relative causal ID.

This completes finite executable regression coverage for the declared V001–V010
reference-kernel spine. It is not external empirical validation of WIF.

## INTEGRATION-001 — End-to-End Pipeline
Connects observation packet, recovery, property image, safe-action intersection,
test selection, immutable freeze/reveal/score, claim-resolution gating, and
optional causal intervention. Integration debugging preserved BUILD-001's
existing `score(FreezePacket, revealed)` API rather than bypassing it.

## INTEGRATION-002 — RED TEAM
Whole-engine claim-resolution attacks: pattern forcing, post-hoc segmentation,
tolerance laundering, scale cherry-picking, observer-created recurrence,
projection-to-ontology collapse, prediction-to-causation collapse, repetition-
to-causation, broad-prediction inflation, unknown-as-zero, and safe-action
overreach.

The suite also includes anti-dogmatism controls: earned causal identification,
finer-measurement resolution, unique projection within a declared class,
unchanged segmentation, and actions supported by the full safe intersection
must remain allowable. A firewall that blocks everything is itself a failure.

## VALIDATION-001 — Foreign Case: NIST StRD Norris
Uses the external NIST Norris ozone-monitor calibration dataset (36 observations).
The adapter computes ordinary least squares from the observations, then compares
against NIST's certified intercept, slope, residual standard deviation, and R²
under declared numerical tolerances. Passing establishes only that this foreign
numerical case matches the certified reference; it is not empirical validation
of WIF as a scientific theory or ontology.

## VALIDATION-002 — Foreign Ambiguity: Sampling Aliasing
A standard signal-processing identifiability problem. Under uniform sampling at
10 Hz, an 8 Hz sine and a -2 Hz sine have the same discrete sample sequence.
The validation requires WIF to preserve both candidates rather than infer the
continuous-time source from aliased samples. Repeating the same sampling map
does not resolve the ambiguity; changing the sampling design to 11 Hz separates
the declared rivals. This tests disciplined ambiguity and lawful resolution
gain, not a WIF-specific toy ontology.

## VALIDATION-003 — Foreign Dynamical Identifiability
A system-identification style case with two dynamical candidates deliberately
observationally identical over a declared training window. The engine must keep
both alive despite dense/repeated observations inside that window, select a
future discriminating time, freeze rival predictions before reveal, score the
reveal, and only then focus to one candidate within the declared dynamic class.
This tests finite-history underdetermination and prospective discrimination.

## VALIDATION-004 — Foreign Causal Identifiability
A standard two-variable causal-identification construction. A->B and B->A
models are deliberately given the same passive joint distribution, so
observation alone cannot identify direction. The models commit prospectively
to different distributions under do(A=1); the intervention reveal can then
identify one model within the declared causal class. The suite preserves the
seeing-versus-setting distinction and forbids passive predictive equivalence
from becoming causal direction.

## VALIDATION-005 — Model-Class Incompleteness
The initial declared model class H0 contains no candidate compatible with the
foreign observation. Recovery must return an empty set and issue a class-relative
failure certificate rather than select the nearest candidate, rewrite the
observation, or widen tolerance. A candidate-class expansion is recorded as a
new version H1; H0 remains failed. H1 may refocus, remain ambiguous, or fail
again. This exercises contradiction -> lawful defocus -> explicit revision ->
new recovery without retroactive rescue.

## VALIDATION-006 — Segmentation / Change-Point Firewall
Raw trace remains first-class. Neighboring one-boundary segmentations can remain
unresolved under a declared SSE tolerance even when segment count is fixed.
Boundary moves, method changes, and tolerance changes are new analyses/versions,
not retroactive rewrites. RAW TRACE != SEGMENTATION; COUNT != BOUNDARY.

## OSC-SEG ADAPTER-001
Connects OSC-SEG to WIF without granting transition boundaries in advance.
Candidate event sets are scored from declared local transition evidence; WIF
recovers a boundary image first, then computes geometric trace lengths for each
surviving segmentation. Boundary ambiguity propagates into length ambiguity.
Resolution and tolerance are logged. The claim gate explicitly blocks segment
recovery from becoming mechanism, recursion, or octave identification.

## OSC-SEG ADAPTER-002 — Event Operator
Replaces hand-granted boundary indices with an explicit transition operator
H(x,phi,C)=0. The minimal executable operator is H=x-(threshold+phi+C), with
declared crossing direction, uncertainty band epsilon, resolution, and version.
The adapter recovers admissible crossing intervals from the sampled trace,
optionally interpolates a crossing time under the declared local model, and
constructs dynamic segments only between recovered successive events.
Zero-crossing evidence does not identify mechanism, periodicity, recursion, or
an exact event time when uncertainty remains.

## OSC-SEG ADAPTER-003 — Event Sets, Metrics, and Blind Ratio Prediction
Propagates crossing-interval ambiguity into admissible event sets, segment
durations, and ratio signatures. Repeated ratios are descriptive only. A
candidate scale/ratio rule earns additional status only through a frozen
unseen-duration prediction and reveal/score cycle. Ratio fit alone does not
establish octave, recursion, a scale law, or a fundamental number.

## OSC-SEG ADAPTER-004 — Operator Competition
Adds a frozen rival set for next-segment prediction: constant, additive,
multiplicative, alternating, and abstaining null. Predictions are frozen before
reveal and scored symmetrically. A target operator may uniquely survive a test,
tie rivals, miss, or face a reveal that kills the whole declared rival class.
A predictive win does not identify mechanism or establish a universal law;
replication and broader null/rival competition remain required.

## STX / OSC-SEG SURROGATE-COMPETITION-001
Introduces an explicit matched-null eligibility audit. A target transition rule
does not earn surrogate advantage merely by predicting correctly: eligible
nulls must preserve the declared nuisance features (here a minimal interface
for mean, variance, and lag-1 structure), predictions are frozen before reveal,
and the target must survive where all eligible matched nulls fail. Weak nulls
cannot confer credit. A surrogate win is test-specific and does not identify
mechanism, causation, or universality. This is an executable first bridge to the
STX Surrogate Principle; it is not yet a full phase-randomization/IAAFT engine.

## STX SURROGATE-GENERATOR-001
Moves from declared matched-null credentials to generated surrogate series whose
features are measured and audited. The initial deterministic families are
cyclic shifts and reversal. Eligibility is computed from declared feature
tolerances; a null that fails the audit cannot confer evidential credit. The
competition packet freezes original series, requirements, generated null
series, audits, null prediction rule, and target prediction before reveal.
This is deliberately NOT called IAAFT or phase-randomized surrogacy: those
stronger generators remain future work.

## STX SURROGATE-GENERATOR-002 — Spectral/Phase Nulls
Adds deterministic Fourier phase-randomized surrogates. Fourier magnitudes are
held fixed and conjugate symmetry is enforced so the reconstructed surrogate is
real-valued. Each generated null is numerically audited against the original
power spectrum before eligibility. This controls the declared linear spectral
structure while changing phase organization. A target win against these nulls
does not by itself identify nonlinearity, mechanism, causation, or universality.
This is phase-randomized surrogacy, not IAAFT; amplitude-distribution matching
beyond the spectral constraints remains future work.

## STX SURROGATE-GENERATOR-003 — IAAFT-style nulls
Adds deterministic iterative amplitude-adjusted Fourier surrogates. Each iteration imposes original Fourier magnitudes and rank-remaps to the original empirical amplitude distribution. Eligibility is measured: both amplitude-distribution and spectral distances must meet frozen tolerances. Finite-iteration spectral matching is approximate. A verified-null win remains test-specific and does not establish nonlinearity, mechanism, causation, recursion, or universality.

## WIF/STX BLIND-COMPETITION-LEDGER-001
Adds repeated prospective competition records. Every trial freezes the target
prediction, rival predictions, tolerance, and version before reveal. Outcomes
are WIN/TIE/LOSS/ABSTAIN. The ledger reports target accuracy separately from
unique-win rate so merely being correct cannot be confused with outperforming
rivals. A single loss breaks the strict persistent-advantage status; ties
preserve rival ambiguity. Finite repeated predictive advantage does not
identify mechanism, causation, or universality.

## WIF/STX BLIND-LEDGER-002 — Dependence + Opportunity Firewall
Adds provenance for source/window and the frozen candidate opportunity set.
Overlapping windows from the same source are connected into dependence
components; raw wins remain visible but are not silently counted as independent
replications. Multiple candidate opportunities are explicitly flagged for
accounting rather than allowing the surviving target to masquerade as a single
predeclared hypothesis. No p-value or probability claim is produced without a
declared statistical model.

## WIF/STX BLIND-LEDGER-003 — Calibrated Statistical Evidence
Probability is admitted only through a frozen statistical plan. The first
supported model is an explicitly declared IID binomial win-count null with
frozen success probability, independent trial count, opportunity count, test
statistic, and alpha. The gate refuses calculation when declared dependence is
present, frozen n disagrees with the ledger, or the opportunity count is
undercounted. Bonferroni adjustment is implemented as a conservative bound for
the frozen opportunity count. A tail probability is P(data-or-more-extreme |
declared null), not P(hypothesis true | data), and it does not identify a
mechanism.

## WIF/STX BLIND-LEDGER-004 — Null-Model Adequacy / Calibration
Adds diagnostic checks before calibrated statistical evidence is released:
observed-vs-declared success-rate calibration, binary lag-1 dependence, and
block-rate stationarity. Thresholds are explicit. Failure withholds the
binomial evidence rather than silently trusting IID. Passing these diagnostics
does not prove IID or the null model true; it only supplies declared diagnostic
support. The diagnostics themselves are not p-values.

## WIF/STX BLIND-LEDGER-005 — Replication / Domain-Transfer Firewall
Types evidentiary recurrence instead of calling every repeated success an
independent replication. Records distinguish same-source repeats, same-specimen
new-source checks, same-population method cross-checks, independent specimens,
different populations in one domain, and cross-domain transfer. Only winning
blind trials contribute to predictive convergence status. Cross-domain
predictive convergence may support transfer of predictive structure; it does
not identify a shared mechanism, shared ontology, or universal law.

## WIF/STX v2.8 — Cross-Domain Invariant Extraction
Winning results may be mapped into a declared relational signature language.
The transferable core is the set intersection of declared signature features
across winning domains. Domain-specific labels therefore drop out automatically.
Representation mismatches block intersection until a mapping is explicitly
declared. Cross-domain wins can legitimately yield an empty invariant core.
A nonempty core is only an invariant of the declared signatures and tested
winning set; it does not identify a common mechanism, ontology, or fundamental
structure. Leave-one-domain-out cores expose features whose apparent
persistence depends on inclusion/exclusion of a domain.

## WIF/STX v2.9 — INVARIANT-MAP-001 Semantic / Representation Mapping Firewall
Cross-domain invariant extraction now requires explicit frozen maps from each
domain representation into a shared target representation. Unmapped features
remain visible rather than being silently coerced. Same words may map to
different relations; different words may map to the same declared relation.
Rival mappings are compared. If rival maps produce different invariant cores,
the engine reports INVARIANT_CORE_MAPPING_DEPENDENT. A mapping never by itself
establishes semantic identity, operator identity, or mechanism identity.

## WIF/STX v3.0 — INVARIANT-MAP-002 Blind Unseen-Domain Transfer
Competing cross-domain mappings now make frozen feature predictions for a
domain not used to construct the mapping. Predictions are scored only after
the target-domain signature is revealed. A unique surviving map earns only
prospective transfer support for that domain. Ties remain ties; all-map failure
remains failure. Broad/empty feature predictions can survive without earning
unique credit. A transfer ledger tracks repeated prospective domain tests.
Even persistent unique map survival does not establish semantic identity,
mechanism identity, or universality.

## WIF/STX v3.1 — INVARIANT-MAP-003 Specificity / Information Firewall
A frozen feature universe now makes prediction commitment explicit. Under the
current subset-compatibility rule, an empty feature prediction is vacuous: it
survives every reveal and has no falsifying outcome. Correct nonvacuous
predictions can therefore be separated descriptively from vacuous survivors.
Among correct nonvacuous predictions, the number of required frozen features
is recorded as set commitment. This is NOT a probability, p-value, likelihood,
Shannon information measure, or truth score. The feature universe itself must
be frozen because commitment fractions depend on it. More committed correct
predictions do not identify mechanism or make the underlying model
automatically truer.

## WIF/STX v3.2 — INVARIANT-MAP-004 Two-Sided Prediction Firewall
Predictions can now freeze both required P+ and forbidden P- features. A hit
requires every required feature to appear and every forbidden feature to be
absent from the revealed signature. Required and forbidden sets must be
disjoint and contained in the frozen feature universe. Constraint count is a
descriptive commitment measure only, not probability, information, likelihood,
or truth. Negative predictions are meaningful only within the frozen
observation/signature protocol and declared feature universe; WIF does not
silently assume a global closed world. Two-sided predictive success still does
not identify mechanism.

## WIF/STX v3.3 — INVARIANT-MAP-005 Constraint Dependence / Redundancy Firewall
A frozen logical implication graph now prevents logically entailed feature
calls from being silently counted as separate commitments. If A=>B, requiring
both A and B has one irredundant positive root rather than two independent
pieces of evidence. Negative constraints are reduced with the dual logic:
forbidding B already excludes A when A=>B. Raw constraint count is preserved
beside the dependency-adjusted effective count. This is logical redundancy
under a declared implication graph only; nonredundancy does not establish
statistical independence, probability, causal separation, or mechanism.

## WIF/STX v3.4 — INVARIANT-MAP-006 Evidence Ancestry / Shared-Support Firewall
Feature commitments now carry declared evidential roots. Features whose support
ancestries overlap are joined into shared-root components, preventing multiple
branches from the same declared evidential trunk from being silently described
as separate support groups. Required and forbidden predictions are both
audited. Missing ancestry is explicit. Disjoint declared roots still do not
prove statistical independence, and evidential ancestry is not causal
ancestry. Support-group counts do not generate probabilities.


## v3.5 INVARIANT-MAP-007
Frozen provenance DAG detects latent shared upstream support (instrument,
calibration, preprocessing, source) even when immediate evidence roots differ.
Provenance is not causality; DAG separation is not statistical independence;
component counts are not probabilities.


## WIF/STX v3.6 — INVARIANT-MAP-008 Provenance Completeness / Unknown-Ancestry Firewall
Each provenance node can now freeze whether its parent list is complete.
No recorded common ancestor is promoted to declared ancestry separation only
when both relevant upstream closures are marked complete. Otherwise separation
remains unresolved. Unknown ancestry is never silently converted into absent
ancestry. Even complete declared separation does not establish statistical
independence.


## WIF/STX v3.7 — INVARIANT-MAP-009 Empirical Dependence / Conditional-Coupling Firewall
Separate provenance trails must now survive an empirical coupling diagnostic.
A prospectively frozen binary-phi plan records minimum sample size and an
absolute coupling threshold. Degenerate marginals and insufficient data remain
unresolved. Conditional strata can be audited without promoting conditional
association to causation. Failure to detect coupling is never proof of
independence, and no p-value is produced without a separately declared sampling
null model.


## WIF/STX v3.8 — INVARIANT-MAP-010 Lag / Lead-Lag Selection Firewall
Lag opportunities are frozen prospectively before scoring. Positive lag aligns
X_t with Y_{t+lag}; negative lag tests the reverse alignment. Each lag records
overlap and binary phi, with insufficient overlap and degenerate marginals
remaining unresolved. The engine reports unique or tied maximum absolute-phi
lags without converting lagged association into directional causation.
Changing the searched lag set after reveal creates a new version. Statistical
significance remains unavailable without a declared null and opportunity
adjustment.


## WIF/STX v3.9 — INVARIANT-MAP-011 Timing Calibration / Lag-Identifiability Firewall
Observed lag is decomposed as process lag plus admissible clock offset and timing
jitter. Frozen timing-calibration bounds generate a set of admissible process
lags. WIF distinguishes exact lag identification, sign-only identification,
and direction unresolved when the admissible set crosses zero. Changing timing
bounds after reveal creates a new version. Even an identified lag sign does not
establish causation.


## WIF/STX v4.0 — INVARIANT-MAP-012 Clock Drift / Time-Warp Firewall
Timing uncertainty now evolves across the observation window under frozen
clock-drift models. For each time, WIF recovers an admissible process-lag
interval and its possible signs. A lag direction is promoted only when its sign
is stable across time and across every frozen admissible drift model. Sign
reversal, zero-crossing, or model disagreement leaves direction unresolved.
The result is explicitly model-class-relative; drift-robust lag direction still
does not establish causation.


## WIF/STX v4.1 — INVARIANT-MAP-013 Calibration / Target Leakage Firewall
Calibration records and target-scoring records are frozen as explicit sets.
Direct record overlap is leakage. Distinct IDs are not enough: the provenance
DAG is traversed upstream, so calibration and target records descending from
the same raw trace, source, preprocessing artifact, or other declared ancestor
are flagged as shared ancestry. If provenance coverage is incomplete, leakage
status remains unresolved rather than clean. Only complete frozen provenance
with no shared declared ancestry is eligible for a blind-claim partition, and
even that does not establish statistical independence.


## WIF/STX v4.2 — INVARIANT-MAP-014 Target Reuse / Adaptive Feedback Firewall
Target exposure is now an append-only, version-aware ledger. A target revealed
to a model version remains exposed to descendant versions; creating a revised
model does not make the old target blind again. Prior exposure outside declared
version ancestry is also disclosed and is not treated as fresh. Only a target
with no revealed exposure in the frozen ledger is eligible for a new blind
claim. Version ancestry cycles and conflicting parent declarations are blocked.


## WIF/STX v4.3 — INVARIANT-MAP-015 Target Novelty / Duplicate-Derivation Firewall
Fresh-target eligibility now audits target identity rather than filenames alone.
The frozen identity model checks same IDs, exact content hashes, declared
derivation ancestry, shared target ancestors, overlapping source windows, and
same-specimen records. Transformed or resampled descendants remain linked to
their revealed target ancestry even when hashes, filenames, windows, or record
IDs differ. A target is called novel only relative to the frozen identity fields
and declared derivation graph; absence of a declared collision is not an
ontological guarantee of independence.


## v4.4 INVARIANT-MAP-016 Sampling-Unit / Cluster-Dependence Firewall
Novel targets are not silently counted as independent sampling units. Shared units or declared clusters form transitive dependence components. Raw target count is preserved beside cluster-adjusted support-component count; the latter is not an effective statistical sample size without a declared model.


## WIF v4.5 — INVARIANT-MAP-017 Three-Valued Feature Reveal Firewall
Closes the v3.2 debt. Every member of a frozen FeatureUniverse is explicitly
PRESENT, ABSENT, or UNKNOWN. Omitted assessments default to UNKNOWN, never
ABSENT. Required predictions earn compatibility only from PRESENT; forbidden
predictions earn compatibility only from explicit ABSENT. UNKNOWN propagates
as unresolved and cannot silently satisfy a negative prediction.


## WIF v4.6 — INVARIANT-MAP-018 Missingness / Observability-Selection Firewall
Three-valued feature state is now paired with an explicit observability record.
UNKNOWN can be generated by instrument limits, frozen threshold rules, or
selection. Target-aware/analyst-selected observability is flagged; incomplete
selection metadata remains unresolved. Reveal states are checked against whether
each feature was actually assessed. A declared protocol does not establish
ignorable missingness or an unbiased view of the world.


## WIF v4.7 — INVARIANT-MAP-019 Case-Selection / Ascertainment Firewall
The frozen sampling frame now distinguishes eligibility from observation and
records how each case entered or failed to enter the analyzed set. Event-
triggered, outcome-aware, analyst-selected, availability, and publication
selection are flagged. Unobserved eligible cases remain explicit. Stratum
coverage is reported. Only a complete declared census is eligible for
unqualified coverage of its frozen frame, and even that does not establish
external population generalization.


## v4.8 INVARIANT-MAP-020 Sampling-Frame / Denominator-Integrity Firewall
The denominator is frozen with membership, inclusion rule, bounds, construction basis, and completeness. Event/outcome/availability/analyst-derived frames are flagged before ascertainment. Completeness is source-scoped, not external-population completeness.


## WIF v4.9 — INVARIANT-MAP-021 Detection-Regime / Coverage-Drift Firewall
Historical rate comparisons now freeze detection regimes with time bounds,
instrument, protocol, coverage, and threshold. Regime overlap is unresolved;
changes in instrument/protocol/coverage/threshold block unqualified temporal
rate comparison. Event times are assigned to regimes explicitly. No recorded
event under weaker coverage is not treated as event absence, and correcting
regime drift requires a declared forward or sampling model.


## WIF v5.0 — INVARIANT-MAP-022 Label / Classification-Regime Drift Firewall
A stable word does not imply a stable operational class. Classification regimes freeze label, rule, threshold, adjudicator and time bounds. Drift blocks unqualified class-rate comparison; harmonization requires a frozen common rule and reclassifiable raw records.


## WIF v5.1 — INVARIANT-MAP-023 Composition / Mix-Shift Firewall
Composition snapshots freeze stratum counts and expose weight drift. Aggregate rates are separated from within-stratum rates. Pure mix shift can move an aggregate while every stratum remains stable. Standardization requires a frozen reference composition and does not itself identify causal effects.


## WIF v5.2 — INVARIANT-MAP-024 Stratum-Definition / Boundary-Drift Firewall
Stratum names are no longer treated as stable identities. Definitions freeze rule, numeric bounds, and boundary semantics. Cross-period comparison is blocked when membership rules drift. Harmonization requires raw assignment variables and a frozen common rule; unchanged units can otherwise move between strata solely because the ruler changed.


## WIF v5.3 — INVARIANT-MAP-025 Covariate / Measurement-Invariance Firewall
Freezes construct, method, unit, window, transform, calibration. Same variable name is not same measured construct. Cross-regime linking requires a frozen mapping plus overlap/calibration evidence.


## WIF v5.4 — INVARIANT-MAP-026 Calibration-Transfer / Domain-Validity Firewall
Calibration support now freezes source domain, variable, numeric range, contexts, and mapping identity. A valid bridge inside its calibration domain cannot be silently extrapolated to new ranges or contexts. Context-specific residual checks prevent a good global fit from hiding local calibration failure.


## WIF v5.5 — INVARIANT-MAP-027 Calibration-Sample / Overlap-Selection Firewall
Audits the evidence used to establish a calibration bridge. Selection basis, context coverage and numerical range are frozen. Good fit in selected mild-condition overlap does not establish full target-domain transfer.
