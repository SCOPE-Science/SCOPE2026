# Independent mathematical audit

## correctness

PASS

Every edge has four neighboring edges, so two colors must split them 2–2. At rungs S_{i-1}+S_i=2 for S_i=T_i+B_i. If S alternates 0 and 2, consecutive top-rail constraints force their common rung first to 1 and then to 0. Thus B_i=1-T_i. Subtracting the top and bottom constraints then gives T_{i+2}=1-T_i, and either rail equation gives R_{i+1}=1-R_i. The top pattern has least period four, so cyclic consistency requires 4|n. When this holds, T_0,T_1,R_0 are three independent bits and recover all indexed assignments, giving exactly eight. For all n≥3 the even Hamiltonian cycle can be alternately colored, with its perfect-matching complement receiving a third color; properness in the cubic graph gives exactly two neighbors of each other color. One color is impossible. In the cube a witness is top 0011, bottom 1100 and rungs 0101; this contradicts the input-degree parity condition literally stated in Kalinowski et al. §3.

## originality

FAIL

The earlier October 18 catalogue record 40a590861d75 already proves the identical finite-simple prism result for every n≥3, with the same named/indexed counting convention, in a theorem also covering twisted ladders. Its proof yields the three-bit classification itself. The cube witness is an instance of that theorem, and the existence of an odd-input-degree counterexample is independently covered by the earlier K_4 result. This is direct existing coverage, not an inference from similar titles or from simultaneous dates.

## value

FAIL

The exact prism census would be useful if unknown, but the full dichotomy and all eight assignments are already supplied. The cube counterexample is automatic from that census, and the parity correction follows from the definition; there is no distinct remaining contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
