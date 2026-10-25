# Independent mathematical audit

## correctness

PASS

For any compactly supported invariant Borel probability under L(x,y)=(1+y-a|x|,bx), integrability gives E[y]=b E[x], hence 1=a E|x|+(1-b)E[x]. Writing P=E[x_+], N=E[x_-], m=P-N yields A P+B N=1 with A=a+1-b>0 and B=a+b-1>0. Since A+B=2a, direct substitution proves x_+-m=2aN/A and m-x_-=2aP/B, where x_+=1/A and x_-=-1/B are exact fixed points. For endpoint equality N=0 or P=0, support lies on one closed half-plane; L is an invertible homeomorphism for b>0, so the compact invariant support is two-sided invariant. The affine branch matrices M_+=[[-a,1],[b,0]], M_-=[[a,1],[b,0]] have characteristic polynomials t^2+at-b and t^2-at-b. Their values at t=0,±1 show exactly one stable and one unstable real eigenvalue under the stated inequalities; bounded bi-infinite branch orbits are fixed. Thus endpoint equality yields the corresponding Dirac atom; every other invariant probability has both signs. The source proof mistakenly attributes exclusion of -1 to A and +1 to B for M_+ (the correct evaluations are p_+(1)=A, p_+(-1)=-B), but both required inequalities hold and the stated hyperbolicity and theorem are valid. Independent SymPy algebra and an exact mixed-sign 2-cycle confirm calculations but are not substitutes for the general proof.

## originality

FAIL

The published 2026-10-04 finding treats the exact same map and parameter domain, every compact invariant Borel probability, the identical sign-amplitude equation (a+1-b)P+(a+b-1)N=1, the same two fixed-point mean endpoints with Dirac rigidity, and the same positive mass in both open half-planes. The new record adds only the two barycenter defect equations, which follow by eliminating P or N from that published equation and m=P-N; no new mathematical conclusion remains. Source chronology qualification: the earlier record carries a 2026-10-04 research/publication date, but the first visible Resultary Git commit was 2026-10-11T13:59:41Z, 57 minutes after the assessed source's first visible Git import at 2026-10-11T13:02:30Z. This is a present-day exact-coverage assessment, not a claim that public import timestamp proves independent discovery priority.

## value

FAIL

The exact sign-amplitude budget and endpoint rigidity are meaningful stationary invariants of a canonical chaotic map, and a sharp sign-crossing benchmark could be useful in a different context. However this particular submission duplicates a distinct published exact theorem on the same natural object and statistic. Its two defect formulas, presented as the chief refinement, are immediate eliminations from that theorem; it adds no new classification, distinct boundary regime, bound, counterexample or non-implied exact fact. Reproducibility of algebra and an alternative proof presentation cannot supply incremental mathematical value for a covered result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
