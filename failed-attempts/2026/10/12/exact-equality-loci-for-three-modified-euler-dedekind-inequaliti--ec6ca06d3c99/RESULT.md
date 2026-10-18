# Exact equality loci for three modified Euler–Dedekind inequalities
## Finding
Let
\[
n=\prod_{i=1}^r p_i^{a_i}\ge 2,
\]
where the \(p_i\) are distinct primes and \(a_i\ge1\). Define
\[
\Phi(n)=\prod_{i=1}^r (p_i^{a_i}-1),\qquad
\Psi(n)=\prod_{i=1}^r (p_i^{a_i}+1),
\]
and let \(\varphi\) and \(\psi\) be the classical Euler and Dedekind functions. Then the equality cases in three inequalities considered by Atanassov are exactly
\[
\psi(n)-\Psi(n)+\varphi(n)-\Phi(n)=0
\iff
n\text{ is squarefree or a prime power},
\]
\[
\Phi(n)+\Psi(n)=2n
\iff
n\text{ is a prime power},
\]
and
\[
\Phi(n)\Psi(n)=\varphi(n)\psi(n)
\iff
n\text{ is squarefree}.
\]
Thus the first equality locus is precisely the union of the other two natural factorization loci.

## Assumptions and scope
The statement is for integers \(n\ge2\). A prime power means \(n=p^a\) with \(p\) prime and \(a\ge1\); squarefree means every exponent \(a_i\) equals \(1\). The formulas for \(\Phi\) and \(\Psi\) above are the modified functions used in the focal 2024 paper. Its later corrigendum corrects Theorem 2.3 and clarifies historical provenance of the modified functions; the present result uses only the definitions and inequalities corresponding to Theorems 2.1, 2.2, and 2.4, not the corrected Theorem 2.3.

## Proof
For a prime-power block \(q=p^a\), put \(t=p^{a-1}-1\). Then
\[
\psi(q)=\Psi(q)+t,\qquad
\varphi(q)=\Phi(q)-t.
\]
Define
\[
E(x)=\psi(x)-\Psi(x)+\varphi(x)-\Phi(x),\qquad
A(x)=\psi(x)-\Psi(x).
\]
If \(m>1\) is coprime to \(q\), multiplicativity gives
\[
E(mq)=\Phi(q)E(m)+2A(m)+t\bigl(\psi(m)-\varphi(m)\bigr).
\]
Every term on the right is nonnegative. Moreover, \(A(m)=0\) exactly when \(m\) is squarefree, and \(\psi(m)>\varphi(m)\) for \(m>1\). For a single prime-power block, \(E(q)=0\). Adding further prime-power blocks therefore preserves equality only while all blocks have exponent \(1\); once a block of exponent greater than \(1\) is present together with another prime support, the displayed recurrence is strict. Hence
\[
E(n)=0
\iff
n\text{ is a prime power or squarefree}.
\]

Next define \(H(x)=\Phi(x)+\Psi(x)-2x\). For a prime-power block \(q=p^a\), one has \(\Phi(q)=q-1\), \(\Psi(q)=q+1\), and therefore \(H(q)=0\). If \(m>1\) is coprime to \(q\), then
\[
H(mq)=qH(m)+\Psi(m)-\Phi(m).
\]
Since \(\Psi(m)>\Phi(m)\), adjoining a second distinct prime support makes the inequality strict. Thus \(H(n)=0\) exactly for prime powers.

Finally,
\[
\Phi(n)\Psi(n)=\prod_i (p_i^{2a_i}-1),
\]
whereas
\[
\varphi(n)\psi(n)=\prod_i p_i^{2a_i-2}(p_i^2-1).
\]
For each \(i\),
\[
(p_i^{2a_i}-1)-p_i^{2a_i-2}(p_i^2-1)=p_i^{2a_i-2}-1\ge0,
\]
with equality exactly when \(a_i=1\). Because all factors are positive, equality of the two products holds exactly when every \(a_i=1\), namely exactly when \(n\) is squarefree.

## Verification
The proof is symbolic and has no cutoff. The accompanying script independently factors every integer \(2\le n\le50000\), evaluates all four functions from their prime-factor formulas, and checks all three biconditionals. Its recorded output is:

`VERIFY_OK n_max=50000 equality_checks=149997`

This finite computation is regression evidence only; it is not used to infer the unbounded theorem.

## Relationship to prior work
Atanassov's 2024 paper defines the two modified functions in the displayed form and proves the three underlying inequalities, but it does not state complete equality classifications for Theorems 2.1, 2.2, and 2.4. The proofs explicitly treat prime inputs as equality cases, while the classifications above identify all equality inputs. The 2024 corrigendum corrects a different statement, Theorem 2.3, and notes that related modified functions had earlier provenance; it does not supply these equality loci. Targeted searches using the formulas, the three equality statements, prime-power language, and squarefree language found no source stating an implication-equivalent classification.

## Limitations
The result concerns only equality in the three displayed inequalities; it does not sharpen their numerical bounds away from equality or give asymptotic information. The modified functions themselves are not claimed to be new: the corrigendum explicitly points to older provenance. The originality claim is limited to the complete equality-locus classification. A residual literature risk remains because an equivalent elementary observation could occur under older notation not indexed by the searched formulas.

## References
1. K. Atanassov, “Two arithmetic functions related to Euler's and Dedekind's functions,” *Notes on Number Theory and Discrete Mathematics* 30(1) (2024), 179–183. DOI: 10.7546/nntdm.2024.30.1.179-183. Online First: 22 March 2024.
2. K. Atanassov, “Corrigendum to ‘Two arithmetic functions related to Euler's and Dedekind's functions’,” *Notes on Number Theory and Discrete Mathematics* 30(2) (2024), 461–462. DOI: 10.7546/nntdm.2024.30.2.461-462. Online First: 25 July 2024.
