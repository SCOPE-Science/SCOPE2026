# Independent mathematical audit

## correctness

PASS

The kernel equation x_(i+1)=x_i+x_(i-1) mod2 has exactly four period-3 solutions when 3|n and only zero otherwise. The image is the codimension-two equality of three parity sums. For a fixed output y of least period p, the necklace predecessor classes are stabilizer R^p orbits on its 4-member labeled fiber. When 3 does not divide p, action has one fixed and one 3-cycle, giving 2. When 3|p and primitive block is reachable, action fixes all 4; otherwise it translates by nonzero 2-torsion, giving 2. Burnside uses H_n(d) fixed reachable strings; Mobius inversion on primitive good blocks yields B4. I independently enumerated all labeled inputs and quotient output fibers for n=1..12, confirming the exact (B0,B2,B4) histograms (2,2,0), (8,5,1), (44,2,14), (256,16,80) at n=3,6,9,12. The nontrivial all-n argument rests on group action/linear algebra, not this finite run.

## originality

PASS

Martin–Odlyzko–Wolfram 1984 gives additive finite-ring algebra and labeled linear image; Frati–Petak–Cheney 2024 investigates 256 binary necklace networks, but its accessible full manuscript does not provide this exact all-length pointwise stabilizer-degree law or Mobius-Burnside class census. A published Rule 90 inverse law concerns a different kernel and cannot directly imply Rule 150 parity conditions. Search could miss old tables or additive-CAs network-degree characterizations; originality is best-of-knowledge.

## value

PASS

This is a natural complete invariant of the rotation-quotient dynamics: it distinguishes 0,2,4 predecessor necklaces despite all reachable labeled outputs having four predecessors. Exact period/parity criteria, census formulas and almost-sure degree-four asymptotics aid classification of finite cyclic cellular-automaton phase space. It is not a mere renaming of labeled linear rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
