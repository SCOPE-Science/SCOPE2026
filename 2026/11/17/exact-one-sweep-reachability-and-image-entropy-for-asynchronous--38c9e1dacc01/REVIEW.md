# Independent mathematical audit

## correctness

PASS

PASS: the local traffic rule is f(left,0,right)=left, f(left,1,right)=right; the three scan equations use old left/right only before update and already updated left plus y0 at the final site. An internal 1->0 transition forces old center 1 followed by next old 0, excluding any cyclic 101 including seam; y[n-1]=1 with y0=0 forces a backward contradiction, and the exceptional (0,1,1,0) seam is incompatible with site0 and final equations. Conversely x_i=y[i-1] OR y_i for 1<=i<=n-2, with explicitly chosen (x0,xlast) in the RESULT.md three cases, satisfies each local equation whenever all three tests hold. Exact four-pair adjacency T forbidding 101 yields I_n=tr(T^n)-(T^n)_{10,10}-(T^(n-2))_{01,10} and stated GF and Pell-like cubic recurrence. Distinct outputs are counted, not preimages. Independently enumerated every input and every target for n=3..10; image-language sets agree exactly. Entire proof covers n>=3 and does not infer long-time dynamics.

## originality

PASS

PASS (best of knowledge): synchronous Rule184 output language forbids 1100 and differs; prior sequential Rule184 literature establishes eventual convergence and has a complete transient-layer census, but its actual theorem does not state the one-sweep image characterization/GF. The current exact boundary-sensitive image test is not logically implied by eventual periodicity or clock census without additional information; different invariant from dynamics.

## value

PASS

PASS: exact recognizability of the image of a fixed sequential traffic rule is a natural global reachability classification with constructive predecessor, finite boundary correction and asymptotic information loss, giving a precise distinction from mass-conserving synchronous traffic. A canonical all-length language is valuable independently of a general theorem for all elementary rules or multi-sweep behaviour.

The dated certificate retains the supplied scientific assessment, sources and limitations.
