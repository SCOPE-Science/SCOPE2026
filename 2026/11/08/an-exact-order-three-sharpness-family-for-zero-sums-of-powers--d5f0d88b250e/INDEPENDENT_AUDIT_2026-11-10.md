# Independent mathematical audit

## correctness

PASS

C PASS. t residue classes imply q mod14 is 9 or 11, e integral, gcd(q,e)=1 and ord_e(q)=3; e_1=gcd(e,q−1)=t. For j=1..13, residues r0=j,r1=[qj]14,r2=[q²j]14,r3=j give base-q digits of je via (q r_prev−r_next)/14 and s_q(je)=t/7*(j+[9j]14+[11j]14). The fourteen normalized digit sums are (3,2,3,2,3,4,3,2,3,4,3,4,3,6), uniquely minimized at j=2,4,8. Any zero-sum length is divisible by t. Length t would have genuine three-digit representation <q³ contradicting that digit minimum; coefficient triples of 2e attain 2t, and all optimal solutions reduce to the three cyclic rotations. The cubic inequality e<(t+1)³−1 holds for t≥4; Dirichlet gives infinitely many prime bases q≡11 mod14 (t=7u+5). Independent exact BFS for t=4,5,11,12 verifies finite shortest lengths; analytic modular orbit argument establishes the infinite family.

## originality

PASS

O PASS, with a specific specialization risk. Breuer–Héthelyi–Horváth–Külshammer (Prop. 2.22, arXiv:1912.03065) already gives a general digit-sum minimization algorithm for all coprime (q,e). The 14-entry spectrum is an elementary evaluation of that method and must not be claimed as a new general algorithm. Jacob–Külshammer (arXiv:2204.09403, Conjecture 4) motivates the k=2 sharpness question but does not list the two complete progressions t≡4,5 mod7, the uniform 2t equality, or rigidity of all optimal triples. Evaluating the nontrivial parameter-uniform orbit and classifying minimizers provides a specific sharpness witness beyond an uncomputed general algorithm. Explicit caution: the prior formula may allow this computation with little extra work, and unindexed equivalent specializations could cover it.

## value

PASS

V PASS. A proposed bound for zero sums of powers is naturally tested by infinite sharpness families, not merely isolated examples. The q³-level family has e/t³→4/7 and exactly three optimal configurations; it shows where the conjectured k=2 constant cannot improve even along prime q. The motivation is the conjecture's extremal boundary and rigidity, not novelty of the generic digit-minimization method; mathematical value here is a self-contained exact infinite family despite its short orbit enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
