# Independent mathematical audit

## correctness

PASS

The final claim quantifies over every positive integer n for the fixed odd prime 971. First, 971 is prime. The known recurrence e_n=(n-1)e_{n-1}-e_{n-2}+1-(-1)^n with e1=e2=1 has period dividing 1942 modulo 971: the coefficients/forcing are 1942-periodic, and independent modular recurrence verifies e_{1943}=e1=e_{1944}=e2=1. Independent iteration on the entire first period yields exactly the three zero residues {388,1554,1942}; all odd indices are thereby excluded by a *finite exhaustive* modular lemma. Second, Givens–Moll 2020 establishes e_{2m}=m A(m), A(m)=Σ_{j=0}^{m-1} Π_{l=1}^{j}(m²-l²). For every integer m>0 and j≥971, Π contains two p-divisible factors at l=r,971-r if m≡r≠0 mod p, or the p²-divisible factor at l=971 if m≡0 mod p; for m<971 the added terms vanish exactly at l=m. Thus A(m) ≡ S(m) mod p² for fixed S(t)=Σ_{j=0}^{970}Π_{l=1}^{j}(t²-l²). Third, independent integer evaluation finds S(194)=S(777)=S(194+971)=S(777+971)=459283=971·473 mod 971², so Taylor expansion forces S'(194)=S'(777)=0 mod 971. Hence A(m) is exactly valuation one for all m≡194 or 777 mod p; both m are p-units so e_{2m} has valuation one. For m≡0 mod p, A(m)≡S(0)=Σ_{j=0}^{970}(-1)^j(j!)²≡383 mod 971, a p-unit; e_{2m} thus has valuation ν_p(m)=ν_p(2m). Remaining classes have valuation 0 by the one-period census. The root classes each have density 1/(2p), and ν_p(n) on multiples of 2p has distribution (p-1)/(2p^{k+1}) at k≥1. This yields P(V=0)=1-3/(2p), P(V=1)=1/p+(p-1)/(2p²), and P(V=k)=(p-1)/(2p^{k+1}) for k≥2. Tonelli/floor-count bounds give the mean 1/p+Σ_{k≥1}1/(2p^k)=1/p+1/(2(p-1)); the infinite tail is bounded by a convergent geometric series. The finite experiments are NOT treated as the infinite proof, which depends on the product congruence and complete period.

## originality

PASS

Best-of-knowledge PASS for the complete all-positive-index 971-adic valuation law, not for the 2026 discovery of the terminal 388 branch, the general product identity, or the subsequently published full even-nonzero-root profile. The 2020 primary paper already proves recurrence/product forms and 2p periodicity, and the 2026 Flórez–Higuita-Diaz–Ramírez primary paper proves terminality at 388. A closely overlapping published Resultary record, "The least prime with a nonsimple even FiboLaplace valuation branch is 971", already determines both nonzero even internal roots 388 and 1554 and proves their terminality. That is expressly credited: those pieces are covered prior findings, regardless of different title. The remaining separately verified statement excludes ALL odd roots modulo 971, handles the distinguished zero residue with a 383-unit calculation, assembles a complete all-index valuation function and proves exact distributions and mean. The prior published even-branch theorem expressly disclaims coverage of odd and distinguished classes; the 2020/2026 primary papers do not supply this complete 971-specific consequence. New work is narrow but mathematically nontrivial as a total prime-specific classification. Unindexed literature and implicit deductions from prior formulas remain historical-priority risks.

## value

PASS

Prime 971 is not arbitrarily selected: it is the first known odd-prime counterexample to simplicity of even FiboLaplace valuation branches, and published work established the exact two terminal even residues. The full exact valuation distribution on *all* n, including a proof that no odd root exists, the distinguished unbounded branch, each valuation density and the natural mean, is a complete structural invariant of that exceptionally motivated sequence. A future user of this exceptional tree can use the exact root support and frequencies rather than extrapolate from even-branch data. The new theorem is narrow and substantially uses previously published machinery and roots, but a complete naturally posed exact invariant is worthwhile; no general all-prime theorem or independent novelty of the elementary density summation is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
