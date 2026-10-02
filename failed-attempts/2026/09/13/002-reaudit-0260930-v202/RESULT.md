# Exact d=9 genus-0 double Hurwitz jump and five-term cut/join decomposition

## Context

Let d=9, genus g=0, nu=(5,4), and r=3 simple branch points.  Compare

- mu_A=(6,2,1),
- mu_B=(3,3,3).

Both pairs are off the resonance walls: the proper subset sums of mu_A are
{1,2,3,6,7,8}, those of mu_B are {3,6}, and those of nu are {4,5}.
The line segment
mu(s)=(6-3s,2+s,1+2s) crosses two resonance walls, at s=1/3 and s=2/3.

The connected double Hurwitz number is normalized as
H=N_trans/9!, where N_trans counts transitive tuples
(a,b,t1,t2,t3) with a,b of the prescribed cycle types and the t_i
transpositions.

## Result

The exact endpoint values are

H_A = 324,
H_B = 40,
H_B-H_A = -284.

Peeling the last transposition in the class algebra gives the exact identity

-284
 = 9  * (F(B,(9,))     - F(A,(9,)))
 + 8  * (F(B,(4,4,1))  - F(A,(4,4,1)))
 + 6  * (F(B,(4,3,2))  - F(A,(4,3,2)))
 + 3  * (F(B,(5,3,1))  - F(A,(5,3,1)))
 + 4  * (F(B,(5,2,2))  - F(A,(5,2,2)))
 = -135 -48 -40 -37 -24,

where F(mu,k) is the disconnected genus-zero degree-9 double Hurwitz number
with two simple transpositions.

The exact factor table is

| k       | F(B,k) | F(A,k) | difference | coefficient | term |
|---------|--------|--------|------------|-------------|------|
| (9)     | 3      | 18     | -15        | 9           | -135 |
| (4,4,1) | 0      | 6      | -6         | 8           | -48  |
| (4,3,2) | 4/3    | 8      | -20/3      | 6           | -40  |
| (5,3,1) | 5/3    | 14     | -37/3      | 3           | -37  |
| (5,2,2) | 0      | 6      | -6         | 4           | -24  |

The five k are precisely the cut/join children of nu=(5,4).  Their
transposition-transition multiplicities are 20,5,5,4,2 respectively, and the
displayed coefficients are M[k,nu]|C_nu|/|C_k|.

This is an exact class-algebra cut/join decomposition of the endpoint
difference.  It is **not** the Shadrin-Shapiro-Vainshtein neighboring-chamber
wall-crossing formula itself.  SSV wall crossing compares chamber polynomials
across one resonance wall; the segment here crosses two walls, and the equation
above groups terms by the final transposition on the nu side rather than by
individual wall crossings.

## Proof / evidence

A direct conjugacy-class transition calculation in S_9 gives

N_A = 117573120 = 324*9!,
N_B = 14515200  = 40*9!.

Transitivity is forced for the endpoint pairs because there is no common
proper subset sum of mu and nu; a disconnected cover would induce such a
common block size.

The transposition transition matrix has exactly five nonzero children from
nu=(5,4):

- (9) with multiplicity 20,
- (4,4,1) with multiplicity 5,
- (4,3,2) with multiplicity 5,
- (5,3,1) with multiplicity 4,
- (5,2,2) with multiplicity 2.

Evaluating the two-step factors gives the table above and therefore the total
-284.  The archived scripts provide independent character-sum and class-matrix
implementations of these values.

## Relation to wall-crossing literature

Shadrin-Shapiro-Vainshtein prove piecewise polynomiality in genus zero and an
explicit difference formula for two neighboring chambers separated by one
resonance wall.  Cavalieri-Johnson-Markwig develop the chamber/wall structure
and extend the framework.  The two-wall path here is consistent with that
framework, but the five-term identity proved in this record is the elementary
last-transposition cut/join identity and should not be labeled an SSV
wall-crossing identity without a separate decomposition into the individual
wall contributions.

## Limitations

No raw enumeration of all S_9 tuples is used.  The exact values are instead
checked through conjugacy-class algebra and independent character
implementations.  The record does not provide the two separate single-wall SSV
contributions along the chosen path.

## Reproducibility

Run the archived scripts:

- `artifacts/char_sum.py`
- `artifacts/t11_gjv.py`
- `artifacts/frobenius2.py`
- `artifacts/t29_final.py`
- `artifacts/t32_smallcross.py`

## References

- S. Shadrin, M. Shapiro, A. Vainshtein, *On double Hurwitz numbers in genus
  0*, arXiv:math/0611442; Adv. Math. 217 (2008).
- R. Cavalieri, P. Johnson, H. Markwig, *Chamber Structure of Double Hurwitz
  Numbers*, arXiv:1003.1805.
- I. Goulden, D. Jackson, R. Vakil, *Towards the geometry of double Hurwitz
  numbers*, Adv. Math. 198 (2005).
