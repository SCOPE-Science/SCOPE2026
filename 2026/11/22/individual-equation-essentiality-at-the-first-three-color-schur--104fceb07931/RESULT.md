# Individual equation essentiality at the first three-color Schur obstruction

## Finding

Let \(T_{14}=\{(a,b,a+b):1\le a\le b,\ a+b\le14\}\). In a three-coloring \(c:\{1,\ldots,14\}\to\{0,1,2\}\), the equation \((a,b,a+b)\) is *violated* if \(c(a)=c(b)=c(a+b)\). Repeated summands \(a=b\) represent one equation; exchanging the two summands does not produce a second equation. There are exactly \(49\) equations in \(T_{14}\).

An equation \(t\in T_{14}\) is *individually essential* if deleting its monochromatic prohibition, while keeping all other \(48\) prohibitions, permits a three-coloring. **Exactly \(29\) equations are essential and \(20\) are inessential.** None of the seven equations with right-hand side \(14\) is essential. There are exactly \(1,350\) colorings with \(c(1)=0\) that violate precisely one equation, and exactly \(4,050\) such colorings with three named colors and no normalization. These are the complete near-optimal colorings, since no coloring avoids all equations. The full per-equation rescue multiplicities appear in `critical_triples.csv`.

For example, after deleting only \(5+5=10\), exactly \(666\) named three-colorings satisfy every remaining equation, whereas deleting only \(6+7=13\) admits exactly \(12\). Deleting any of the seven equations that introduce \(14\) admits none.

## Assumptions and scope

The domain is precisely the integer interval \(\{1,2,\ldots,14\}\) and all \(49\) equations \(a+b=c\) with positive summands, \(a\le b\) and \(c\le14\). A three-coloring may use any subset of the three named colors. Every equation is tested individually, not as an arbitrary collection of deletions. Multiplicities count named colorings; normalization fixes \(c(1)=0\) without changing the proportions because the three colors may be permuted.

## Proof

The proof has an analytical rigidity step and a finite complete enumeration.

**Rigidity for the new right-hand side.** A standard classification of Schur-free three-colorings of \(\{1,\ldots,13\}\) (Kisner, Section 4.2) states that, after permuting colors, the three fixed color classes away from \(7\) are \(\{1,4,10,13\}\), \(\{2,3,11,12\}\) and \(\{5,6,8,9\}\), and \(7\) may belong to any one of them. The claim is also exhaustively rechecked by `verify_rigidity.py`. In these classes the monochromatic representations \(1+13=4+10=14\), \(2+12=3+11=14\) and \(5+9=6+8=14\) provide two different equations for each of the three possible colors of \(14\). If removing one sum-\(14\) equation admitted a coloring of all remaining equations, its restriction to the first thirteen integers would have to be Schur-free. Whichever color was assigned to \(14\), at least two sum-\(14\) equations would still be monochromatic, a contradiction. Thus all seven new right-hand-side equations are individually inessential. Note the difference between the whole family of new equations being collectively indispensable and no one of them being indispensable alone.

**Exact equation-deletion census.** Enumerate the \(49\) ordered representatives \((a,b,a+b)\) in increasing \(a\), then increasing \(b\), with \(a\le b\). Every coloring may be permuted so that \(c(1)=0\), leaving exactly \(3^{13}\) assignments. For every assignment compute the list of monochromatic equations. If there are none, increment \(Z\); if there is exactly one with index \(j\), increment \(N_j\). An assignment that satisfies all equations except \(j\) is exactly an assignment counted by \(N_j\), because the known unsatisfiability of the full system, also independently checked, excludes zero-violation solutions. For each equation the deletion survivor count is \(3N_j\); the factor of three counts the possible named colors of integer \(1\). Both supplied implementations enumerate these assignments completely and agree with every entry of `critical_triples.csv`. They produce \(Z=0\), \(\sum_jN_j=1350\), \(\#\{j:N_j>0\}=29\), and \(N_j=0\) for all \(j\) ending at \(14\). Consequently the named count with exactly one monochromatic equation is \(3\cdot1350=4050\).

For computational completeness, the C++ implementation assigns integers sequentially and checks only equations whose right-hand side has just been assigned. The number of violations never decreases as the coloring is extended; therefore pruning a partial assignment after its second violation cannot omit a coloring with at most one violation. Every unpruned branch is completed, and every completed branch is scored by its unique violated equation or none. The independent Python implementation enumerates all \(3^{13}\) words without pruning, builds three color bitmasks, and directly checks the full equation list; thus the two programs have distinct traversal and scoring methods. The third script independently enumerates all valid normalized colorings of the first thirteen integers and verifies the rigid classes and the double-violation argument for \(14\). This is a complete finite proof for the stated interval, not an extrapolation from smaller samples.

## Verification

The source code and canonical CSV travel with the theorem. With Python 3 and a C++17 compiler installed, run from their shared directory:

```text
python3 verify_rigidity.py
python3 verify_direct.py
g++ -std=c++17 -O2 verify_incremental.cpp -o verify_incremental
./verify_incremental
```

The expected assertions are respectively: six normalized Schur-free thirteen-integer colorings with the rigidity property; zero normalized defect-free fourteen-integer colorings, \(1350\) normalized one-defect colorings, \(29\) essential equations and no sum-\(14\) essential equation; and independent C++ agreement with the entire 49-row CSV. The executables are not necessary to interpret the CSV, and no external solver or corpus is required.

## Relationship to prior work

The classical value \(S(3)=13\), stated here as the first obstruction occurring at integer \(14\), and the classification of Schur-free three-colorings of the first thirteen integers are **not** claimed as new. Kisner (2013) explicitly supplies the finite three-class structure. Thanatipanonda (2008/2009) studies numbers of monochromatic Schur triples in large colorings, obtaining asymptotic bounds, including for at least three colors, but not this exact \(49\)-equation deletion classification. Chappelon, Revuelta Marchena and Sanz (2013) consider modular Schur numbers, whose existence results do not directly determine individual standard-equation sensitivity. The contribution here is the exact named per-equation deletion spectrum and the structural observation that all seven newly introduced equations are individually inessential. Searches of relevant published research records did not identify a statement covering this spectrum; that does not establish absolute priority.

## Limitations

The census concerns precisely three named colors, the interval through fourteen, and deletions of exactly one equation; it says nothing about deleting multiple equations, larger intervals or other palette sizes. Its numerical table relies on two complete but computational enumerations, whereas the seven-new-equation obstruction follows from the credited thirteen-integer classification. Historical coverage can be incomplete; independent scholarly validation and publication-priority certification have not been performed.

## References

1. T. Thanatipanonda, *On the monochromatic Schur triples type problem*, arXiv:0801.0798 (first posted January 5, 2008); *Electronic Journal of Combinatorics* 16 (2009), R14. https://arxiv.org/abs/0801.0798
2. S. L. Kisner, *Schur's Theorem and Related Topics in Ramsey Theory*, M.S. thesis, Boise State University (May 2013), especially Section 4.2. Public manuscript: https://andrescaicedo.wordpress.com/wp-content/uploads/2013/05/summer-kisner-thesis-final-version.pdf
3. J. Chappelon, M. P. Revuelta Marchena and M. I. Sanz Domínguez, *Modular Schur numbers*, arXiv:1306.5635 (first posted June 24, 2013); *Electronic Journal of Combinatorics* 20(2) (2013), P61. https://arxiv.org/abs/1306.5635
