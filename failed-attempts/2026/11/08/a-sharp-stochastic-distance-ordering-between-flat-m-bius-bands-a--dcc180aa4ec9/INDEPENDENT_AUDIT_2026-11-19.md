# Independent mathematical audit

## correctness

PASS

The infinite-strip deck action gives squared distance D_M^2=min(t^2+(y1-y2)^2,(a-t)^2+(y1+y2)^2); the matched cylinder uses min(t,a-t)^2+(y1-y2)^2. For independent uniform y_i∈[-b,b], the absolute sum/difference (S,V) have constant density 1/(2b^2) on S,V>=0,S+V<=2b; hence P(S<=u or V<=v)=L_b(u+v) and P(S<=z)=L_b(z). The independent horizontal difference has density 2(a-t)/a^2. Integration yields the claimed two CDFs, whose integrands satisfy L_b(u+v)>=L_b(max(u,v)). For 0<=r<=a/2, supports of u,v do not overlap. For a/2<r<R_C, around t=a/2 both u,v>0 and max(u,v)<2b, so a positive-measure strict gap exists. For r>=R_C=sqrt(a^2/4+4b^2), max(u,v)>=2b throughout. At r=a/2+epsilon, only |t-a/2|<epsilon contributes; min(u,v)=sqrt(a epsilon)sqrt(1-|s|)+O(epsilon^(3/2)), L_b(u+v)-L_b(max)=min(u,v)/b+O(epsilon). Integrating with weight 1/a and ∫[-1,1]sqrt(1-|s|)ds=4/3 gives 4/(3b sqrt(a))epsilon^(3/2)+O(epsilon^2). Compact support and the strict CDF gap imply strict positive-moment inequality. Independently reconstructed the complete seven-blob canonical Git tree and its source-tree SHA; a separate SciPy quadrature at (a,b)=(1,.35),(2,.4),(3,2) checked equality/strictness and onset ratios approaching one as epsilon decreased 1e-3 to 1e-5. Numeric checks are not used as infinite proofs.

## originality

FAIL

Two actual earlier published full primary findings cover the entire submitted claim. October 25, 2026 "Distance statistics detect the half-twist of a flat Möbius band" states the identical strict/equality intervals and identical O(epsilon^2) 3/2-onset after C=a,H=2b, plus stronger reconstruction. November 2, 2026 "A complete two-point distance ordering for the flat Möbius band and its matched cylinder" independently states the identical two-parameter quotient and full excess distribution integral after L=a,h=b and includes stronger terminal and coupling laws. The newer November 8 claim does not isolate any non-implied mathematical remainder. The three primary RESULT.md texts were actually read in full, not inferred from search snippets.

## value

FAIL

The exact geometric two-point comparison, all-radius strictness classification, 3/2 onset with sharp coefficient, and all-positive-moment consequence are mathematically meaningful but are already proven for the identical matched flat quotients in published 2026-10-25 and 2026-11-02 work. The submitted conditional triangle integration is an algebraically equivalent derivation of the prior complete CDF-excess law. No independently motivated new invariant, non-implied corollary, boundary case, or quantitative improvement survives the prior coverage. Re-presenting an identical theorem with a second proof and routine integral normalization is not a valuable original research finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
