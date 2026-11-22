# Independent mathematical audit

## correctness

PASS

Read full frozen RESULT.md, inspect the actual 4096-pair `verify_transfer.py` and verified tree path inventory. A time-three-fixed cell has exactly four possible histories (always resting or one of three 0→1→2 phases); local exact-two Moore firing in each of 3 rows and times defines necessary/sufficient triples of 64-state columns. Cyclic length-n walks in the 4096 pair graph biject with labelled torus F^3-fixed configurations for n>=3. Independently re-implemented the local constraints: obtained 12,286 graph edges, 2,125 active vertices, unique cyclic SCC with 184 vertices and 559 internal edges. Independently reconstructed exact integer/symbolic 184×184 characteristic polynomial x^156 Q(x)^2 R(x) and initial traces S3=1,S4=145,S5=181, matching the claimed zeta. Only all-rest is time-one fixed; hence C3=(S_n−1)/3 and n4 has 48 orbits. The attached program's positive Perron vector and integer Collatz–Wielandt inequalities give the strict 3.26505918..3.26505920 interval (vector was identified at actual package path, not independently recalculated in this audit); primitivity from strong connectivity and a self-loop yields trace asymptotic. Neither small-n enumeration nor saved logs alone proves all n: the finite graph bijection and exact characteristic check do.

## originality

PASS

The classic Brian's Brain rule, unrestricted-plane three-cycles and transfer-matrix enumeration methods pre-exist and are credited. The specific three-row B2/S/C3 Moore torus temporal-three symbolic zeta with degree-28 spectral factor, sharp circumference-four onset and spectral radius bound was not found in inspected comparable sources. Read full published two-row Brian's Brain rigidity result (two-row offset collisions) and separate two-row Wireworld results; their graph incidence, matrix and numbers differ, so they do not imply the three-row polynomial. Jen's 1988 cylindrical CA framework is a method, not this exact computed invariant. Accessible historical sources incomplete; originality is best-of-knowledge.

## value

PASS

Exact primitive temporal 3-cycle populations for every circumference of the first distinct-offset three-row Brian's Brain torus form a natural complete classification of a well-established CA rule. The rational spatial zeta polynomial, exact onset and rigorously confined entropy base quantify nontrivial population growth, rather than one arbitrary tiny instance. Computer algebra certification of the natural transfer graph is part of a finite exact self-contained invariant, not an excuse to equate computation with value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
