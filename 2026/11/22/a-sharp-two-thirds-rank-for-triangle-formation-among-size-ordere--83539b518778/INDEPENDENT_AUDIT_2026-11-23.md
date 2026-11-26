# Independent mathematical audit

## correctness

PASS

The n−1 independent uniform cuts give Dirichlet(1,…,1) spacings, represented by normalized independent unit exponentials. The common factor cancels from size ordering and the strict triangle inequality; with exponential order gaps Y_j, failure at ranks i,i+1,i+2 is E_(i)≤Y_(i+2). The exponential joint density on its ordered cone factors in the gaps with rates n−j+1, so Y_(i+2) is independent of E_(i) and the Laplace product from m+2 through n equals the stated factorial ratio. The next/current failure ratio is (m+1)(n+m)/[2m(2m+1)]; for integer n and m≥2 it is less than one exactly when n≤3m−2, and otherwise strictly greater. Thus the minimum occurs at m=floor((n+1)/3), also including n=3,4, with no ties; n=3 yields the classical success probability 1/4. For the asymptotic, write x=m/n: the Stirling exponential has rate f(x)=2x log(2x)−x log x−(1+x)log(1+x) and prefactor 2 sqrt(2/(1+x)) to relative O(1/n) near 1/3. Since f'(x)=log(4x/(1+x)), f(1/3)=log(3/4) and m−n/3 is bounded, optimizing integer rounding affects the ratio only at order 1/n. This gives sqrt(6)(3/4)^n(1+O(1/n)) and i*/n→2/3. Replay: RESULT.md proof lines 30–59 and the explicit Stirling calculation above. The inspected verify.py and VERIFICATION.md concern finite checks; neither is the universal proof.

## originality

PASS

The supported distinct claim is the complete fixed-consecutive-size-rank probability profile for uniform cut spacings, with a strict finite optimizer and its sharp exponentially small failure. The normalized exponential machinery and classical three-piece result are background. The nearest inspected exact broken-stick results change the event quantifier or the sampling law; the nearest indexed rank-specific result uses Pareto inputs. The finding is not a historical priority certification.

## value

PASS

For the natural triangle test on successive size ranks, the risk profile shows that neither end of the size order is optimal for n≥5. It gives a unique finite optimal location and the sharp failure constant across sample sizes, distinguishing this selection rule from global existence or random sampling of triples. This is a motivated structural probability law rather than the computation of a few classical cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
