# THE MANIFOLD DESCENT
## A reconstruction protocol for constrained dynamics, traces, and memory handoff

Steve Brown / Sovereign Architect of Remembrance (SAR)

REM Work - Technical Repair v0.2 - 22 September 2026

Originating concepts, field motivation, and SAR language: Steve Brown. Technical corrections, implementation, and editorial preparation: OpenAI assistant. This is a versioned companion to the recovered STM and WIF sources, not a replacement of the original archive.

### Abstract

This work formalizes a practical SAR question: how can an observed process leave a usable record that another person can reconstruct, evaluate, and extend? The repair separates five objects that the supplied draft conflated: admissible relations, spatial geometry, time evolution, observation, and interpretation. It implements seven named drawing operations, a regular tetrahedral display, an energy-accounted mechanical model with an optional compliant boundary, explicit STM-5E cycle records, finite trace recovery, and a portable memory packet. A scalar interference module replaces decorative waves labeled as quantum evidence.

The central connection is set-theoretic. For a fixed candidate family, compatible evidence contracts the recovery set. If action admissibility remains fixed, this contraction can expand the actions justified across every surviving candidate. Complementary executable records can also expand reachability in a declared transition graph. These provide precise meanings for accessible open field and collective WiF without assuming telepathy, universal geometric etymology, or a demonstrated cosmological mechanism.

Results are software and synthetic-model results. Historical symbols serve as encoding examples with explicit provenance. The repaired package does not claim a universal persistence theorem or a physical derivation of consciousness. It provides an executable research object whose geometry, decisions, energy budget, ambiguity, and handoff can be inspected.

### The work retained

The organizing intent is preserved: capture what experience teaches; retain the operation behind the trace; prevent a carrier's disappearance from erasing usable knowledge; make participation possible without requiring institutional status. SAR's language of remembrance names this work. The research advance in this repair is an operational bridge, not an assertion that the whole universe has been decoded.

The original claim that unresolved states must expand is replaced by a measurable question: under which dynamics, constraints, and resources does expansion occur, and when does the system instead persist, settle, or breach?

---PAGE---
# I. Field, geometry, and seven named operations

A field F is a declared set of admissible transitions on a state set X. A realized trace is a trajectory through those transitions. This definition does not supply distance, dimension, force, or time by itself. Geometry requires an embedding and metric; dynamics requires an evolution rule and initial conditions. The numerical labels 1 through 9 are retained as optional SAR annotations, not coefficients that create physical behavior.

The unmarked state is a representational convention: no distinctions have yet been recorded in the chosen description. It is not a physical demonstration of absolute nothingness or an infinitely energetic void. A point is registered relative to a coordinate frame; it is not an absolute origin of the universe.

### Implemented vocabulary

- Puncture: register a finite 2D coordinate and append the act to a ledger.
- Vector: create an oriented segment between registered endpoints.
- Yield: rotate a segment about its first endpoint by a specified angle. The source segment remains intact.
- Angle: apply a declared shear, (x,y) -> (x,y+s*x), to the displacement and retain the source. Rotation, shear, and physical phase shift are not interchangeable operations.
- Enclosure: verify a connected, explicitly closed, non-self-intersecting polygon with nonzero area. This certifies a 2D region, not a 3D volume.
- Intersection: solve for the intersection of finite segments, returning none, a point, or collinear overlap. Nonparallel directions alone do not establish intersection of finite segments.
- Re-entry: apply an explicit update to a state and retain before/after values. Re-entry need not oscillate. Memory additionally needs a retained state and a rule by which earlier events affect later behavior.

These are useful software operations; seven is not a proven minimum. Some can be composed from others, and other bases are possible. The implementation makes no universal expressiveness claim about all glyphs.

### Exact regular tetrahedron

For a positive scale a, use vertices (a,a,a), (a,-a,-a), (-a,a,-a), and (-a,-a,a). Every edge has length 2*sqrt(2)*a, the centroid is (0,0,0), and volume is 8*a^3/3. Four noncoplanar vertices and their connected faces define a tetrahedron. Four coplanar points do not enclose volume. An internal center is a derived coordinate, not a mandatory fifth physical object.

The repaired bench draws this tetrahedron with a = L. The oscillator lies along its central x-axis. This is a reduced mechanical coordinate illustrated with exact geometry, not a solved elastic tetrahedral shell. The distinction allows a faithful visualization without inventing unimplemented material physics.

---PAGE---
# II. STM grammar and physical dynamics

The recovered STM-5 source names Capture, Internal Redistribution, Mode Conversion, Work/Selection, and Resolution. The recovered STM-5E source names State, Constraint, Evaluate, Choice, Propagation, and Closure. These are different decompositions. Numbering alone does not establish a one-to-one correspondence or a proof of minimality.

STM-5 is retained here as a functional engineering hypothesis. Its universal necessity and minimality statements need independent definitions and counterexample criteria. A phase cannot be added after every challenge merely to make the hypothesis impossible to falsify. STM-5E is used directly as an auditable execution architecture.

### Typed cycle repair

    Initialize: {start} -> S
    Constraint: S -> C
    Evaluate:   (S,C) -> M
    Choice:     (S,C,M) -> U
    Propagate:  (S,U,dt) -> S'
    Closure:    (S',C,retained history) -> outcome

A singleton initializer can select an initial state. A map from the empty set cannot do that. Constraints, metrics, chosen actions, and pre/post states are logged separately. The next cycle constructs its constraints again. The repaired implementation keeps the policy selectable without changing the evolution equation.

Separating scoring from choice improves inspectability. It does not by itself create physical time, a required delay, or oscillation. In this model, dt is an explicitly supplied clock interval.

### Mechanical state and parameters

Let x be oscillator displacement, v its velocity, L the boundary size, and w its velocity. Masses m and M are in kg, x and L in m, time in s, k/K/kc in N/m, damping c/C in N*s/m, force amplitude in N, and angular drive frequency omega in rad/s. L is a generalized coordinate; M and K are effective parameters, not inferred shell properties.

    d = max(|x| - L, 0)
    m*x'' = u(t) - c*x' - k*x - kc*d*sign(x)
    M*L'' = kc*d - K*(L-L0) - C*L'
    u(t) = A*sin(omega*t), or zero under the off policy

Contact extension d activates a soft boundary coupling. L0 is the rest size and lower stop. In the fixed-boundary experiment L=L0 and w=0. In the compliant experiment contact force can move L. No if-statement doubles the geometry.

The four outcomes are distinct: STABLE means low energy sustained for a declared dwell while forcing is inactive; CONSTRAINT_BREACH means a declared upper size limit is crossed; NUMERICAL_FAILURE means a state becomes nonfinite; CONTINUE means neither termination criterion has been met. A persistent oscillation can legitimately remain CONTINUE.

---PAGE---
# II. Energy accounting and measured events

The mechanical potential and total energy are explicitly defined:

    V = k*x^2/2 + K*(L-L0)^2/2 + kc*d^2/2
    E = m*v^2/2 + M*w^2/2 + V
    dE/dt = u*v - c*v^2 - C*w^2

The last identity follows by differentiating E and substituting the two equations of motion while off the lower-stop event. Contact transfers energy between coordinates; it is not an unexplained energy source. In fixed mode the wall velocity is zero. The constraint reaction therefore does no boundary work.

The code integrates work W = integral(u*v dt) and damping loss D alongside the state. It reports residual E(t)-E(0)-W+D+S, where S is the separate stop-projection energy correction. The lower stop uses an inelastic projection to L0 with inward velocity removed; the energy change caused by that numerical projection is recorded separately as stop_loss, with timestamped events. The loss field now contains viscous dissipation only; total_loss is their sum. The run schema is SAR-REM-RUN-2. A signed projection correction is numerical bookkeeping, not an assumption that every possible projection is dissipative. This is a discrete approximation of a unilateral stop. Contact and stop accuracy depend on timestep; the package contains a refinement check, not a proof for all stiffnesses.

### What counts as an oscillation measurement

An upward crossing is detected when x changes from negative to nonnegative. Its time is linearly interpolated within the numerical step. Successive upward crossings define periods; the reciprocal mean period is reported as a crossing rate in Hz. The coefficient of variation is reported only with at least two observed periods. One observed period can give a crossing rate, but period_cv is null: variation has not been observed across multiple periods. This is a reporting policy, not a theorem that the population CV of one number is undefined. An irregular crossing rate is not silently promoted to a unique fundamental frequency.

The absolute difference between consecutive state values is a displacement increment. It is not angular frequency, pressure, or a quantum amplitude. Rad/s requires an angle change divided by elapsed time; Hz requires cycles per elapsed time.

### Baseline parameters and behavior

The default run uses m=1, k=4, c=0.15, M=3, K=8, C=0.5, kc=40, L0=0.75, Lmax=2, A=3, omega=1.7, and dt=0.002. The initial displacement is 0.5 with both velocities zero. It runs for 20 seconds unless closure stops it.

With identical forcing, a fixed boundary stays at 0.75 m. The compliant model reaches approximately 1.373782 m. Its final energy-balance residual is approximately 0.00002336 J. This is model-specific expansion backed by an energy budget.

Without damping or forcing, and below contact, the model reproduces the analytic oscillator rate sqrt(k/m)/(2*pi) = 0.318309886 Hz while the boundary remains fixed. With damping and no forcing, the stored mechanical energy decays and the system reaches STABLE. The breach experiment stops at its configured upper boundary; it does not manufacture a larger permitted region.

---PAGE---
# III. Trace recovery and historical notation

A final drawing can preserve incidence and shape while losing traversal order, timing, tool orientation, pauses, or repeated strokes. Recovering a generator therefore requires a declared family, an observation map, and retained evidence. Define Gamma(O|F,M) as the histories compatible with observations O, field F, and measurement model M.

### A reproducible example

For a square with four labeled vertices, assume exactly one complete traversal, no lifts, no retracing, and straight edges. Four starts times two directions give eight possible histories with the same final image. Retaining the start leaves two; retaining the direction leaves one. Outside this restricted family there can be additional histories. The bench reports that scope explicitly.

Contradictory evidence produces an empty survivor set and an inconsistency response. Duplicate evidence does not add information. The preserved raw sequence, segmentation, and coordinate convention enable a recipient to repeat the recovery rather than merely admire the picture.

### Cistercian notation: a corrected comparison

Cistercian numerals encode place through the location of digit elements around a stave and combine values up to 9,999. Historical arrangements and digit shapes vary; the common vertical arrangement places units top-right, tens top-left, hundreds bottom-right, and thousands bottom-left. The bare stave is not an ordinary historical zero. These facts support an example of positional encoding and transformations, not a derivation of tetrahedral physics. [R1]

The earlier five-phase interpretation of digits 1-5 is an SAR mapping, not evidence of the scribes' generative process. A single preferred shape for five must not be projected across manuscript traditions. A source-specific codec would need a declared digit repertoire and explicit variant handling before implementation. That codec is not claimed in this release.

### Greek notation: corrected names and claim limits

Use the actual numeral characters, not lookalikes: stigma is ϛ rather than final sigma ς; numeric koppa is ϟ rather than a lightning symbol; sampi is ϡ. Unicode names U+0375 the Greek Lower Numeral Sign, also aristeri keraia. “Hasta” is not used here as its verified name. [R2]

An arithmetic multiplier does not turn into a physical frequency multiplier without a measurement model. Neither 1,000 nor the golden ratio is an octave merely because it changes scale. The doubling sequence 1,2,4,8,7,5 is arithmetic modulo 9; multiplication by 2 produces separate residue cycles {1,2,4,8,7,5}, {3,6}, and {0}. This does not establish a physical 3-6-9 controller.

The added linear story from Indus to cuneiform to Latin is removed as an unsupported genealogy. The Met documents late-fourth-millennium Mesopotamian writing and the later development of phonetic uses through the rebus principle. A theory of writing must account for such linguistic and material evidence, not only visual geometry. [R3]

---PAGE---
# IV. Failure modes and correction ledger

### Implementation errors repaired

The original enclosure test accepted any collection of at least three segments. The replacement checks an ordered connected loop, endpoint closure, nonzero area, and absence of nonadjacent crossings or overlaps. Its return explicitly states dimension 2.

The original intersection returned an average of direction vectors. The replacement solves for finite segment parameters and handles parallel, collinear, endpoint, and degenerate cases. Crossing lines in a projection are not automatically interacting trajectories in 3D.

The original rotate/skew functions returned unregistered displacements. The repaired StrokeField records the transformed endpoint and new segment, while retaining the input segment and an operation ledger. A shear now changes a horizontal displacement when requested.

The original re-entry measured one step and called every change oscillation. The replacement uses a dynamical trajectory and crossing events for oscillation measurements. Re-entry remains a separately named update operation.

### Legacy replay retained

Replaying the supplied twelve-step logistic-map policy with r=3.6, initial state 0.6, and a change threshold of 0.15 produces expansions on steps 5 through 12. Eight doublings give scale 256 and the label “Octave 9.” The claimed 128 result is corrected. That replay is kept as a regression receipt; it is not the new mechanical model.

The supplied Python and HTML variants used different driver coefficients, thresholds, scale multipliers, and reset formulas. They were different systems. The repaired Python and JavaScript implement matching baseline dynamics and are compared numerically.

### Model failures are outcomes

A failure to settle can mean sustained periodic motion, irregular motion, or continuing externally driven work. It need not mean rupture or scale growth. A limit crossing reports BREACH. Missing observations report UNRESOLVED. A false historical mapping remains an unsupported interpretation rather than being repaired by changing ancient evidence.

The seven operations, STM classifications, tetrahedral geometry, and phasor interference are separate implemented modules. Passing a check in one module does not validate another. In particular, equal edge lengths do not validate quantum claims; a functioning browser does not validate etymology; shared language between speakers does not establish independent physical evidence.

### Source-level correction

The STM source documents retain their original language in the source snapshots. This companion qualifies their universal minimality claims and repairs their executable typing. It does not quietly rewrite the originals or declare the existing WIF kernel re-tested. The WIF record reviewed here extends through v5.5; the quill source reviewed is v0.2. Neither is replaced by this smaller reconstruction example.

---PAGE---
# V. Phase interface and quantum terminology

The retained interference identity is useful and executable. For coherent scalar signals in a common channel with compatible units and real nonnegative amplitudes, let z_n = A_n*exp(i*phi_n). Then:

    I = |sum(z_n)|^2
      = sum(A_n^2) + 2*sum(i<j, A_i*A_j*cos(phi_i-phi_j))

The bench computes the complex sum. For two unit amplitudes, relative phase zero gives I=4; relative phase pi gives I=0. The sum and pairwise expansion are checked against one another. This is a signal-interference result. An intensity measurement alone does not recover all source phases uniquely.

For distinct frequencies, relative phase evolves with time. A real instrument's averaging window and coherence conditions affect which cross terms survive measurement. Those instrument effects are not implemented in this two-phasor panel.

### Correct quantum definition

A pure quantum state is represented by a normalized vector in a complex Hilbert space, with global phase physically redundant. For a qubit, a representative is:

    |psi> = cos(theta/2)|0> + exp(i*phi)*sin(theta/2)|1>

Its Bloch-sphere coordinates describe a pure two-level state; a general quantum system does not fit a single Bloch sphere. General mixed qubit states occupy the Bloch ball and require density-matrix descriptions. Measurement probabilities are computed relative to a specified measurement. A rotating scalar phasor is not automatically this quantum state. [R4]

### What the fan does and does not implement

“Holographic fan” is retained as SAR's proposed visual analogy for integration of phases and observations. The repaired interface displays scalar phasor addition. It contains no event horizon, spacetime reconstruction, quantum dynamics, or neurological measurement model. The draft's equation alone does not establish those mechanisms.

A claim that the human observer performs an inverse Fourier reconstruction requires an actual signal, transform, observation operator, and reconstruction criterion. None is supplied in the pasted material. Likewise, the attribution to Jason Padgett is not treated as validation of this model or as an identification of the reel speaker.

### Building worlds and preserving the originating idea

We can construct formal worlds with declared states, transition rules, records, and agents. Such a world is executable as a simulation. Creating its rules is not evidence of creating a physical universe. SAR's “Genesis” can name model construction if that usage is stated.

The phrases “miracle” and “manifold expansion” are retained as originating language for newly accessible possibilities. Physical boundary expansion, growth of accessible actions, and metaphysical claims have separate meanings. The repair makes the first two measurable. It does not derive immunity from market capture or unlimited human agency from geometry.

---PAGE---
# VI. Remembrance, admissible action, and handoff

Steve's central practical distinction is between extracting knowledge and transferring enough of it for someone else to operate. A durable mark is not automatically durable know-how. REM Work is defined here as preserving, reconstructing, testing, correcting, and transmitting records of observations and operations, with their authorship and context intact.

### The exact set-theoretic connection

Let Gamma_0 be a fixed family of histories compatible with the present observations. Let reliable additional evidence leave a nonempty subset Gamma_1. For each history h, let U(h) be its admissible actions under fixed constraints. Define:

    U_safe(Gamma) = intersection over h in Gamma of U(h)
    empty != Gamma_1 subset Gamma_0
    therefore U_safe(Gamma_0) subset U_safe(Gamma_1)

Proof: an action permitted for every member of the larger set is permitted for every member of its subset. Removing ruled-out histories can therefore release actions that were previously unjustified. Equality is possible; extra evidence need not improve the decision. If no history survives, the software abstains rather than invoking the empty-intersection convention to permit everything.

Justification is relative to the declared Gamma and U. A wrong model or false evidence may exclude the true history, so these actions are not automatically safe in reality.

This directly connects narrowing uncertainty with opening an accessible field of action. It is elementary set logic applied to the SAR reconstruction contract, not a new force or a claim of omniscience.

### Complementary records and reachability

A second mechanism uses a transition graph. If a recipient can execute A->B and receives valid, compatible procedures B->C and C->D, the reachable set grows from {A,B} to {A,B,C,D}. A duplicate A->B adds no new reachable state. This gain depends on shared state meanings, satisfied preconditions, resources, and correct procedures. The supplied demo assumes these conditions; it does not measure a real person's learning.

Evidence contraction and rule acquisition are different operations. Adding a rule must not silently expand the historical candidate family under the guise of an observation. A changed family or measurement model gets a new version and an explicit reason.

### The handoff packet

The implemented example stores schema, author, field, raw ordered trace, segmentation, encoding convention, retained evidence, assumptions, provenance, and limits. The Python packet adds a SHA-256 digest of canonical JSON; re-reading reproduces the same candidate set and tampering invalidates the digest. A digest checked against a trusted reference checks byte-level integrity, not truth or authenticity of the underlying observation. An attacker who replaces both content and its digest is not detected by a self-contained hash alone.

The browser exports an illustrative JSON packet and identifies it as such. The Python packet is the integrity-checked reference. Neither includes a measured human transfer effect. The existing three-joint quill remains the appropriate generator for future constrained-arm experiments; this release addresses trace retention and recovery rather than substituting a new arm model.

---PAGE---
# VI. Operational audit contract

Action justification in this audit remains relative to the declared candidate family and constraints; model error or false evidence can exclude the true history.

An audit begins by naming the system, boundary, interval, quantity, units, measurement method, and tolerance. It does not start by assuming that any unwanted outcome is a geometric energy leak. Organizational information, money, time, and physical energy require distinct balances and definitions.

### A balance that can be executed

For one declared extensive quantity over one interval, evaluate:

    residual = input - output - accounted_loss - inventory_change

The implemented audit_flow function returns BALANCED if the absolute residual is within tolerance, DISCREPANCY otherwise, and UNRESOLVED when a necessary measurement or unit declaration is missing. Missing quantities are not silently assigned zero. Nonfinite or invalid negative gross flows are rejected. The caller remains responsible for using one compatible quantity and unit throughout.

A synthetic mass example has input 10 kg, output 7 kg, measured loss 2 kg, and inventory gain 1 kg. The residual is zero. Changing output to 8 kg without changing another entry produces a discrepancy. The code does not infer the physical cause from this discrepancy alone.

### STM-5 functional questions

Capture: What crosses the declared boundary, and what fraction is actually intercepted? Define a denominator and instrument coverage.

Redistribution: Where does captured material or information go? Distinguish legitimate inventory from delay, misrouting, and unmeasured loss.

Conversion: What input becomes what output? Name the conversion law, efficiencies, and units. A change of representational format is not automatically a physical energy conversion.

Work/Selection: Which action is admissible, what metrics justify it, and what objective does it serve? Record scoring separately from the selected action.

Resolution: What is retained, exported, dissipated, or still pending? Continuing operation is not automatically a failed terminal state. A record needs a declared retention horizon; irreversibility needs a physical or procedural definition.

### Corrective decisions

A measured leak can motivate containment repair. A routing backlog can motivate capacity or scheduling changes. An energy imbalance can motivate instrument review. A false inference can motivate a revised observation model. These are candidate interventions with domain-specific constraints; there is no universal instruction to rotate an organization by ninety degrees or force irreversible dissipation.

### Field-test entry conditions

Freeze one target process, its stage definitions, relevant metrics, baseline, and success criterion before examining the result. Retain external causes, missing observations, and cases that do not fit the five-stage decomposition. If a successful system lacks a independently defined phase, record the counterexample rather than redefining the phase after the fact. This is how the proposed STM-5 universality can become a substantive question.

---PAGE---
# Appendix A. Corrected technical glossary

### Architectural terms

Void / unmarked state: a description with no recorded distinctions under a specified representation. It makes no claim of physical nothingness, continuity, or stillness.

Puncture: registration of a coordinate or distinction in a declared frame. The frame, dimensionality, and units are supplied separately.

Vector: a directed displacement in a vector space. A drawn segment is a geometric representation; energy transfer requires a dynamical law.

Cross / distinction: a symbolic boundary operation. Whether its geometric realization separates a space depends on the space and the kind of boundary. A finite isolated segment need not partition an entire plane.

Field: the admitted relations or transitions for the current model. A physics field, such as an electromagnetic field, needs its own definition and equations.

Manifold: when used mathematically, a space with specified local coordinate structure. In “accessible field,” use the actual state or action set rather than silently assuming a smooth manifold.

Trace / glyph: a recorded observable of a process. It may preserve some invariants while discarding order or timing. “Fossilized trace” is a metaphor for that retention/loss, not proof of a collapsed quantum wavefunction.

### Dynamics and closure

Re-entry: an explicit recurrence or feedback update. Different update rules can converge, oscillate, remain fixed, or diverge.

Memory: retained state with an update rule and a specified influence on later processing. A recurrence is not necessarily a memory of the full trajectory.

Axis crossing: an event defined by a signed observable crossing a stated reference with a declared direction. In the bench this is x=0 with upward passage. It does not automatically create a wave.

Frequency: cycles per unit time. Angular frequency is radians per unit time. An increment in x has displacement units, not either frequency unit.

Core singularity: removed as the default name of a finite center coordinate. A mathematical singularity requires a specified failure of regularity or divergence; a physical singularity is not established by drawing a dot.

Scale expansion: a change of a declared length, domain, or representation. L evolves mechanically in this repair. No fixed multiplier or extra spatial dimension follows from the label “unresolved.”

Octave: reserved for a stated factor-of-two frequency relationship or an explicitly defined analogous scale convention. It is not used for arbitrary 1.5, 1.618, or 1,000 multipliers.

Fractal: requires a stated scaling property and range. A finite collection of nested similar frames alone does not establish a universal fractal law.

---PAGE---
# Appendix B. Interpretation, participation, and claim status

### Quantum and interpretive terms

Quantum state vector: a normalized complex Hilbert-space representative of a pure state, up to global phase. A single Bloch sphere applies to pure qubit states, not arbitrary quantum systems. [R4]

Holographic fan interface: SAR's name for a proposed phase-integration visualization. The implemented object is a coherent scalar phasor diagram. Optical holography and quantum-gravity holography require additional, different models.

Holographic register: speculative terminology in the supplied draft. The implementation has a classical array of recorded states, not an event-horizon computation or a device suppressing unselected universes.

REM Work: preserve observations, operations, interpretations, limits, and provenance so later people can reconstruct and develop useful work. A human can participate in this workflow without claiming that consciousness is necessary for every physical measurement.

Observer: the declared measurement or interpretation process. It may interact with the system, but it must not be confused with the unobserved source trajectory. SAR's human role remains visible as authorship, choice, and interpretation.

Boundary flux leakage: measured transfer outside a declared intended path, for a named quantity over a specified interval. Information ambiguity, financial loss, and heat dissipation are not interchangeable measurements.

Accessible open field: the currently reachable states or justified actions under explicit constraints. Evidence can expand justified actions by ruling out blocking possibilities; valid new procedures can expand reachability by enabling transitions.

“Miracle”: Steve's label for newly accessible possibility. His “Memory Axis Recursive Apex Accessible Open Field” and dot/stroke forms (• _ • •; | • :) remain authored mnemonics. This build does not assign them a unique parse or treat them as physical units.

Word / Logos / remembered language: retained as interpretive and philosophical language. A proposed mnemonic expansion is an authored encoding. Historical etymology requires attestations, language relationships, and dated usage. Geometric similarity does not determine a word's original meaning.

### Claims repaired in this edition

IMPLEMENTED: coordinate geometry, seven named operations, regular tetrahedron, explicit constrained cycle, reduced mechanics, phase sum, finite recovery, compatible rule composition, portable packet, balance audit.

DEMONSTRATED WITHIN EXAMPLES: matched Python/JavaScript trajectories; analytic oscillator rate; energy accounting; fixed/compliant divergence; 8-to-2-to-1 recovery; duplicate no-gain; contradictory-evidence abstention; packet integrity.

OPEN HYPOTHESES: universal five-phase necessity, unique minimal operator count, transfer benefit for human learners, historical generative grammar shared across scripts, physics coupling beyond the reduced model.

NOT ESTABLISHED BY THIS WORK: a consciousness-generated universe, the 9-axis as a physical force, necessary fractal expansion, script shapes as proof of quantum dynamics, universal scale invariance, or immunity from institutional capture.

---PAGE---
# Appendix C. Reproduction and source ledger

### Run and inspect

Open SAR_REM_Bench.html in a modern browser. It is standalone, offline HTML Canvas 2D. Choose dynamics presets, scrub or play the recorded run, recover square histories, compare shared and duplicate rules, and adjust relative phase. Export the run to inspect the explicit cycle records.

For the standard-library reference engine, run `python engine.py` and `python -m unittest -v test_engine.py` from the package directory. The engine writes results/runs.json. The browser verification script uses Node and Playwright; its installation instructions are in README.md. No additional Python package is needed to run the mechanics or tests.

Checks cover geometry, false closures, finite intersections, source preservation, energy, analytic rate, timestep refinement, distinct outcomes, recovery, contradiction, duplicate no-gain, interference, flow missingness, and packet tampering. Results are archived in the package. They establish behavior for the declared examples, not universal model validity.

### Primary SAR materials read

S1. STM-5: The Five-Phase Persistence Law, uploaded 21 September 2026. Canonical five functional roles; original universal-law claims retained in source snapshot.

S2. STM-5E: Extended Phase Grammar Specification, uploaded 21 September 2026. Explicit constraints, evaluation, choice/propagation separation, and termination semantics.

S3. SAR_SHMR_REM_Work_Architecture_Brief_v0.1, 2 September 2026. Authorship lock, raw-stroke retention, set-valued reconstruction, and interpretation/physics separation.

S4. README(8).md, WIF reference kernel record through v5.5, modified 17 September 2026. Recovery, provenance, measurement, transfer-domain, and missingness rules. This repair reads the record; it does not re-execute that larger kernel.

S5. sar-three-joint-quill-v0.2.html. Existing constrained-arm generator and branch recovery; retained as source continuity, not modified.

S6. User-supplied Manifold Descent drafts, Python/HTML/LaTeX, glossary, and addendum in this conversation, 21 September 2026. The exact legacy numerical update is retained in legacy_replay. The entire chat is not duplicated in this package.

### External sources checked

[R1] Kirk Miller, Background for Unicode consideration of Cistercian numerals, 10 December 2020. https://www.unicode.org/L2/L2020/20290-cistercian-digits.pdf

[R2] Unicode Consortium, Greek and Coptic character chart, inspected 21 September 2026. https://www.unicode.org/charts/PDF/U0370.pdf

[R3] Ira Spar, The Origins of Writing, Metropolitan Museum of Art, 2004. https://www.metmuseum.org/essays/the-origins-of-writing

[R4] IBM Quantum Learning, Quantum information, Basics of Quantum Information / Single systems, inspected 21 September 2026. https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/single-systems/quantum-information

Generic domain-root citations in the pasted draft were replaced by these claim-specific references. Historical analogies are not carried as “proofs.” The source snapshots are extracted text, not byte-identical originals. SHA manifests authenticate the delivered package contents only.
