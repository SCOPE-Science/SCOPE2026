# Independent mathematical audit

## correctness

PASS

Every point x is contained in exactly 4/h distinct translates, so depth >=3 requires h=1. Given h=1, depth3 requires a positive-branch split 2/2 on queries x,y, equivalent to |A∩(A+y−x)|=2. Then four joint-label populations are 2,2,2,N−6, all ≥2 for N≥8, hence each supports a final separating query; no depth4 because the positive branch has at most four hypotheses. h=4 yields depth1, all other cases depth2. At prime p≥11 Sidon translates are exactly absence of repeated off-diagonal differences; r(t)=3 forces r(2t)=2, giving the dichotomy. Normalized (13,4,1) difference sets are exactly four, each with 13 translates, giving 52 of 715 Sidon supports. Independent enumeration verified p11 has zero and p13 52 such sets, matching proof.

## originality

PASS

PASS for all 4-point translate classes over finite abelian groups and the exact stabilizer/autocorrelation online-dimension criterion. Classical Sidon and Singer difference-set counts are acknowledged, as are general Littlestone/thicket definitions and cyclic-window special cases. The inspected literature did not supply this precise classification or the VC=2 versus Ldim=3 comparison; possible theorem under additive combinatorics/model-theory aliases remains a risk.

## value

PASS

Complete natural four-point translation-family classification with a sharp Sidon boundary, stabilizer behavior and explicit adaptive/static shattering separation. This combines difference-set structure and online learning dimensions, not an arbitrary finite instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
