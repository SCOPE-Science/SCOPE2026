# No transfer-killed 2-torsion at five points on Theta_(2,3,4): structural torsion-freeness, with ordered rank bounded 3..189

## Context
The target asked for a Z/2 class in H_2 of the ordered configuration space F_5(Theta_(2,3,4)) that is killed by the covering projection to the unordered space. The Abrams cubical model, followed by a verified free-face collapse and its 120-sheeted ordered lift, gives a direct structural answer.

## Result
The requested class does not exist. The lifted collapsed model is two-dimensional, so

H_2(F_5(Theta_(2,3,4));Z)=ker(d_2)

is a subgroup of the free abelian group C_2 and is therefore torsion-free. In particular it contains no nonzero Z/2 class, regardless of the covering map.

Downstairs, the exact rational/integral calculation gives

H_2(B_5(Theta_(2,3,4));Z) = Z^3.

The current artifacts do **not** rigorously certify the previously claimed exact ordered rank 189. They compute rank(d_2)=31731 over F_2,F_3,F_5,F_7,F_1000003, which implies rank_Q(d_2) >=31731 and hence

rank H_2(F_5;Z) <= 31920-31731 = 189.

Transfer for the 120-sheeted cover is injective on the free group H_2(B_5;Z)=Z^3 (because p_* tau =120 id), so rank H_2(F_5;Z) >=3. Thus the certified ordered statement is

H_2(F_5(Theta_(2,3,4));Z) = Z^r for some 3 <= r <=189.

## Evidence
- The unordered Abrams complex has counts (462,1512,1785,920,198,12), with d^2=0 verified.
- Verified free-face collapse leaves a subcomplex with counts (202,467,266,0,0,0).
- Unordered ranks over Q give H_2(B_5;Z)=Z^3 because C_3=0.
- The ordered lift has (24240,56040,31920) cells and C_3=0; every lifted face is present and d_1 d_2=0 over Z. Hence ordered H_2 is free.
- Modular sparse elimination gives rank(d_2)=31731 over five primes, yielding the rigorous upper bound r<=189, not an equality over Q.

## Limitations
The exact ordered rank remains open within this package. Proving r=189 requires an exact rational/integer rank certificate or an independent theorem giving the missing upper bound on rank(d_2).
