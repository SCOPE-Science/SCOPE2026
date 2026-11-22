# Independent mathematical audit

## correctness

PASS

PASS. The exactly stated subshift is Fix(G_n²) with G_n=R_n^{-1}F_n, F the synchronous elementary Rule 6 map f(a,b,c)=(1−a)(b xor c), and R left shift. This is *not* Fix(F_n²) except for particular spatial period. Coordinatewise F_n²x=R_n²x is the five-bit predicate f(f(a,b,c),f(b,c,d),f(c,d,e))=e. Four-bit de Bruijn states abcd and edges abcd→bcde satisfying the predicate give a 16×16 integer adjacency matrix; each closed rooted length-n walk corresponds bijectively to an indexed ring solution, with overlapping positions even for n=3. Independently constructed that matrix directly from the truth table and computed exact characteristic polynomial t^10(t−1)(t+1)^2(t³−2t²+2t−2); its determinant gives spatial zeta 1/[(1−z)(1+z)^2(1−2z+2z²−2z³)] and B_n=1+2(−1)^n+u_n with u_{n+3}=2u_{n+2}−2u_{n+1}+2u_n (u0=3,u1=2,u2=0). Direct trace values n=3..10 are 1,11,11,15,15,35,55,83, matching a separate direct finite-ring computation in original verification source. Dominant cubic root α≈1.543689012692 exceeds complex pair modulus sqrt(2/α)≈1.138..., proving growth α^n and entropy log α. F commutes with spatial shift; F_n^2x=R_n^2x implies F_n^{2n}x=x, so solutions are genuine temporally periodic waves. n=1,2 are formal overlap transfers in the zeta; physical statement n≥3. Inspected verification/check_rule6.py source; neither a logged success nor a finite enumeration substitutes for exact 16-state characteristic polynomial.

## originality

PASS

PASS at qualified best-of-knowledge level, and significantly limited by close primary precedent. Koller–Hudcová (arXiv:2508.09768, 2025) explicitly formulate *left-translated two-step cycles for Rule 6*, give general transfer-matrix equations (20)–(21), and plot corresponding entropy profiles. Thus neither the Rule 6 shifted predicate, positive translated-wave entropy in general, nor the matrix method is novel. Their inspected full article does not state the exact all-length Rule 6 spatial periodic-point polynomial, the six nonzero eigenvalues, or the rational Artin–Mazur zeta displayed here; the surviving contribution is that precise nontrivial natural invariant. The published 256-rule temporal-two zeta census concerns *unshifted* Fix(F²), so does not mechanically specialize to Fix(R^-2F²). However older program output or unindexed Rule 6 tables may already contain these exact coefficients, an especially material residual priority risk. Do not present this as a new theory of traveling waves. Crucially, the primary author's supplementary CSVs were now read at the exact Rule 6, p=0,c=2,left-translation row: eigenvalues.csv already reports leading λ≈1.5436890126920757 and second λ≈1; table_entropy.csv already reports s≈0.43417501466531766. These numerical leading-rate values are definitely prior coverage and are NOT original in this record. The remaining mathematical assertion for originality is the full exact all-length spatial zeta denominator, all trace coefficients and recurrence; the archived CSVs do not list these.

## value

PASS

PASS, narrowly. Counting the spatially periodic solutions of the natural co-moving equation F²=R² for Rule 6 is a motivated exact invariant of a positive-entropy traveling-wave subshift. The explicit rational zeta and all-ring recurrence give finite-size counts and primitive spatial necklace numbers, more informative than a plotted thermodynamic-limit entropy. The general transferred-cycle method and known Rule 6 entropy diagrams reduce methodological originality; value rests on the previously unlisted exact closed-form invariant, not novelty of zeta rationality in finite-type shifts or of CA translation patterns. No downstream theorem is necessary for this natural all-length classification. The leading entropy/rate is already numerically known in the authors' 2025 tables; no independent value is assigned to rediscovering it. The added value is the precise complete rational zeta/full fixed-length recurrence beyond that numeric table, though it is a specialized and relatively accessible transfer evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
