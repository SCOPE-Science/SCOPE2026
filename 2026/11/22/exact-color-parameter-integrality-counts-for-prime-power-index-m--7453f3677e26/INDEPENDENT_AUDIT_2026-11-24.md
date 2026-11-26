# Independent mathematical audit

## correctness

PASS

With L=l+1 and K=(p^r-1)L, the denominator outside the multinomial is a power of p, and Legendre gives v_p=r-s_p(K)/(p-1). Folding K's digits preserves its residue mod p^r-1; a cyclic carry decreases their folded total by p-1, including when r=1. A positive vector cannot become zero in one carry. The terminal vector, now consisting of digits, encodes a positive multiple in [1,p^r-1], hence is all p-1. Equality occurs exactly with no carry. At H=qr+t, the t longer columns have q+1 positions and the others q; weak compositions of p-1 in each column already satisfy the digit caps. These strings are positive multiples and only L=1 is removed. For arbitrary X, bracket m(floor(X)+1) between consecutive powers of p, using a strict upper digit cutoff even at equality; H differs from log_p X by O_{p,r}(1). Both endpoint counts have the same leading term with error O_{p,r}(H^{r(p-1)-1}). Independently: python3 /workspace/independent_checks.py 3 compares exact factorial numerator/denominator divisibility and the p-unit conclusion throughout ten bounded ranges, including p=2, r=1, a cutoff with no eligible L, and nonzero t; counts were 7,19,26,23,15,35,26,24,27,0. These runs are corroboration; the general result follows from the digit proof.

## originality

PASS

The supported distinct claim is the complete per-column condition for the prime-power-minus-one fixed index, together with the exact varying-color counts and growth. Neither the published fixed-color results nor general multinomial carry valuations provide this column condition and count by substitution alone. The count itself is elementary once the column condition is proved. This is a best-of-knowledge decision, not a priority certification.

## value

PASS

Fixing a natural exceptional index from the published integrality theory asks the complementary question of which colors are integral. Exact column counts and their asymptotic distinguish an infinite but density-zero set, including its precise growth order and constant; neither a finite table nor a list of candidate exceptions supplies that information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
