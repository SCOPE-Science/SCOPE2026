# Automorphically equivalent cosets in cyclic-center class-two \(p\)-groups

## Finding

**Theorem.** Let \(p\) be an odd prime, \(k\ge 2\), and \(G\) a finite nonabelian \(p\)-group such that \(Z(G)\cong C_{p^k}\) and \(|G'|=p\). A pair \((G,N)\) is called *automorphically equivalent* when \(1<N\lhd G\), \(N<G\), and every \(x\notin N\) has its full coset \(xN\) contained in its \(\operatorname{Aut}(G)\)-orbit. Write \(\Omega_k(G)=\{g\in G:g^{p^k}=1\}\). Then

\[
\{N:(G,N)\text{ is automorphically equivalent}\}=
\begin{cases}
\{G'\},&\exp(G)=p^k,\\
\{G',\Omega_k(G)\},&\exp(G)=p^{k+1}.
\end{cases}
\]

Here \(\Omega_k(G)\) in the second case is a characteristic subgroup of index \(p\). Both exponent cases occur for every \(p,k\) and every rank \(n\ge1\), where \(|G|=p^{2n+k}\). In particular, the number of automorphically equivalent proper nontrivial normal subgroups is exactly one or two, regardless of \(n\) and \(k\).

## Assumptions and scope

All groups are finite; \(p\) is odd, \(k\ge2\), and \(G\) is nonabelian with cyclic center of order \(p^k\) and derived subgroup of order \(p\). The center need not equal the derived subgroup; in fact it is strictly larger here. The result classifies **every** nontrivial proper normal subgroup satisfying the stated coset condition. No claim is made for \(p=2\), noncyclic centers, or derived subgroups larger than order \(p\). We use \([g,h]=g^{-1}h^{-1}gh\).

## Proof

**1. Symplectic reduction and the two normal forms.** Conjugation by \(G\) on \(G'\cong C_p\) is trivial: its image is both a \(p\)-group and a subgroup of a group of order \(p-1\). Thus \(G'\le Z=Z(G)\), and \(G\) has class two. Choose \(c\) generating \(Z\), and put \(z=c^{p^{k-1}}\), which generates \(G'\). Since \([g^p,h]=[g,h]^p=1\), the quotient \(V=G/Z\) is an \(\mathbb F_p\)-vector space. The pairing
\[
B(\bar g,\bar h)=b\quad\Longleftrightarrow\quad[g,h]=z^b
\]
is alternating, bilinear and nondegenerate: its radical consists exactly of the central elements. Hence \(\dim_{\mathbb F_p}V=2n\) for some \(n\ge1\), and \(|G|=p^{2n+k}\).

The map \(\lambda:V\to Z/Z^p\cong\mathbb F_p\), \(\lambda(gZ)=g^pZ^p\), is well defined and linear. The first assertion follows because multiplying by \(c^a\) changes the \(p\)th power by \(c^{ap}\). For linearity, the class-two identity \((gh)^p=g^ph^p[h,g]^{\binom p2}\) has its last factor equal to one since \(p\) is odd and \(|G'|=p\). As \(Z/Z^p\) is one-dimensional, either \(\lambda=0\) or \(\lambda\ne0\). In the first case all elements have order dividing \(p^k\), and a central generator has order \(p^k\). In the second case some \(g^p\) generates \(Z\), so \(g\) has order \(p^{k+1}\). No exponent larger than \(p^{k+1}\) is possible because every \(p\)th power lies in \(Z\).

In the \(\lambda=0\) case, choose a symplectic basis of \(V\) and lift it to elements \(x_1,y_1,\dots,x_n,y_n\). Each lift has \(p\)th power in \(Z^p\), so multiplication by a suitable central element makes its \(p\)th power one. We may arrange \([x_i,y_i]=z\), all cross commutators trivial, and \(x_i^p=y_i^p=1\).

In the \(\lambda\ne0\) case, choose \(x_1\) with \(x_1^p=c\), where this equation defines a generator \(c\) of \(Z\). Express the now scalar-valued functional \(\lambda\) uniquely as \(\lambda(v)=B(v,\bar y_1)\), using the commutator generator \(z=c^{p^{k-1}}\) and the identification \(cZ^p\mapsto1\). Nondegeneracy of \(B\) guarantees the existence and uniqueness of \(\bar y_1\). Because \(x_1^p=c\), we have \(\lambda(\bar x_1)=1\), and hence \(B(\bar x_1,\bar y_1)=1\). Alternation gives \(\lambda(\bar y_1)=B(\bar y_1,\bar y_1)=0\), so we may choose an order-\(p\) lift \(y_1\) of that vector by correcting its \(p\)th power with a central power. The orthogonal complement of the symplectic plane \(\langle\bar x_1,\bar y_1\rangle\) is contained in \(\ker\lambda\), since every vector in that complement is orthogonal to \(\bar y_1\); thus it has a symplectic basis with order-\(p\) lifts. In summary, with a suitable symplectic basis the relations are
\[
 c^{p^k}=1,\quad [x_i,y_i]=c^{p^{k-1}},\quad
 x_1^p=c,\quad y_1^p=1,\quad x_i^p=y_i^p=1\ (i\ge2),
\]
with all cross commutators trivial and \(c\) central. These presentations follow from the preceding lift construction. The first case has the same relations with \(x_1^p=1\). For explicit existence and cardinality, use coordinates \((u,v,a)\in\{0,\ldots,p-1\}^{2n}\times(\mathbb Z/p^k\mathbb Z)\), and write \(\delta=0\) for the first presentation or \(\delta=1\) for the second. Define
\[
(u,v,a)(u',v',a')=
\left( u+u'\bmod p,\ v+v'\bmod p,\
a+a'-p^{k-1}\sum_{i=1}^n v_i u_i' +\delta\left\lfloor\frac{u_1+u_1'}p\right\rfloor\bmod p^k\right).
\]
The bilinear term and the ordinary integer-carry cocycle make the multiplication associative, and the displayed elements \(c=(0,0,1)\), \(x_i=(e_i,0,0)\), \(y_i=(0,e_i,0)\) satisfy the indicated relations. All \(p^{2n+k}\) tuples are distinct, verifying that both presentations occur for every permitted parameter and giving the normal-form uniqueness used below.

**2. The derived subgroup always qualifies.** If \(g\notin Z\), the nondegeneracy of \(B\) gives \([g,G]=G'\), so its conjugacy class is exactly \(gG'\). If \(g=c^a\in Z\setminus G'\), write \(a=p^va_0\) with \(0\le v\le k-2\) and \(p\nmid a_0\). For each \(t\in\mathbb F_p\), there is an integer unit \(u\equiv1\pmod p\) with \(ua\equiv a+tp^{k-1}\pmod{p^k}\). In either standard presentation, the assignment
\[
 c\longmapsto c^u,\qquad x_i\longmapsto x_i^u,\qquad y_i\longmapsto y_i
\]
respects all relations and induces an invertible action on \(V\) and on \(Z\). It is therefore an automorphism, sending \(c^a\) to \(c^{a+tp^{k-1}}\). This covers every coset \(gG'\) for \(g\notin G'\), proving \((G,G')\) is automorphically equivalent.

**3. No other central subgroup qualifies.** Every nontrivial subgroup of the cyclic center is \(N=\langle c^{p^j}\rangle\) with \(0\le j\le k-1\), and \(G'=\langle c^{p^{k-1}}\rangle\). If \(j\le k-2\), take the noncentral generator \(y_1\) of order \(p\). Then \(y_1\notin N\), but \(y_1c^{p^j}\in y_1N\) has order \(p^{k-j}\ge p^2\). These two elements are not automorphically equivalent. Thus a central \(N\) must be \(G'\).

**4. Restriction on noncentral subgroups.** Let \(N\lhd G\) be noncentral. Since \(N\) contains a noncentral element and \([N,G]\le N\), nondegeneracy implies \(G'\le N\). If \(Z\not\subseteq N\), a central \(c\notin N\) has coset \(cN\) containing both central and noncentral elements, which cannot be automorphically equivalent. Therefore \(N\ge Z\). Such normal subgroups correspond to proper vector subspaces \(W=N/Z<V\).

If \(\lambda=0\), choose any \(\bar v\in V\setminus W\), with an order-\(p\) lift \(g\) as in step 1. Since \(c\in N\), the elements \(g\) and \(gc\) belong to the same external \(N\)-coset but have orders \(p\) and \(p^k\). The condition fails for every \(W\).

Suppose \(\lambda\ne0\). If \(W\not\subseteq\ker\lambda\), some \(w\in W\) satisfies \(\lambda(w)\ne0\). For any \(v\notin W\), the affine line \(v+\mathbb F_pw\) contains vectors of zero and nonzero \(\lambda\); their lifts have orders at most \(p^k\) and exactly \(p^{k+1}\), respectively, and they lie in one external \(N\)-coset. This again fails. If \(W\subsetneq\ker\lambda\), choose \(v\in\ker\lambda\setminus W\) and adjust a lift by a central element to obtain an element \(g\) of order \(p\). Then \(g\) and \(gc\) belong to one external \(N\)-coset but have different orders. The only remaining possibility is \(W=\ker\lambda\).

**5. The index-\(p\) possibility is sufficient.** For \(\lambda\ne0\), the set \(\Omega_k(G)\) is the full inverse image of \(\ker\lambda\), since \(g^{p^k}=1\) precisely when \(g^p\in Z^p\). It is therefore characteristic and has index \(p\). The complement consists exactly of elements of order \(p^{k+1}\). We show it is a single automorphism orbit.

In the standard presentation, \(\lambda(\bar g)=B(\bar g,\bar y_1)\), where \(B\) uses \(z=c^{p^{k-1}}\) as generator. For any \(g\notin\Omega_k(G)\), put \(c'=g^p\), which generates \(Z\). Then
\[
[g,y_1]=(c')^{p^{k-1}}\ne1.
\]
The plane spanned by \(\bar g,\bar y_1\) is symplectic. Its orthogonal complement lies in \(\ker\lambda\) (because it is orthogonal to \(\bar y_1\)). Choose a symplectic basis of this orthogonal complement with lifts of order \(p\); the latter exist by multiplying by suitable powers of \(c\). Along with \(g,y_1,c'\), these lifts satisfy precisely the second presentation in step 1 and generate all of \(G\). Thus there exists an automorphism taking \(x_1\) to \(g\). Consequently \(\operatorname{Aut}(G)\) is transitive on \(G\setminus\Omega_k(G)\), and \((G,\Omega_k(G))\) is automorphically equivalent. Combining steps 2–5 proves the theorem.

## Verification

A standalone Python 3 checker `checker.py` constructs both types with \(p=3\), \(k=2\), \(n=1\), each of order 81. For each it independently verifies the multiplication law and presentation, enumerates every subgroup and normal subgroup, constructs **all** automorphisms from generator images satisfying the defining relations and generation condition, and tests the external-coset condition against their exact orbit partition. The first type has 41 subgroups, 29 normal subgroups, and exactly the eligible subgroup of order 3. The second has 14 subgroups, 11 normal subgroups, and exactly the eligible subgroups of orders 3 and 27. These are finite checks only; the proof above covers all \(p,k,n\).

Run `python3 checker.py` using standard-library Python. The expected terminal marker is `CYCLIC_CENTER_AUTOMORPHIC_COSET_CHECKS_OK`.

## Relationship to prior work

McCulloch and Tărnăuceanu (arXiv:2611.11746, initially public November 9, 2026) define automorphically equivalent pairs and classify them in finite abelian groups; they explicitly ask for other important finite-group classes. The present theorem classifies all such pairs in a nonabelian, unbounded-rank class having cyclic centers strictly larger than their commutator subgroups.

Kumar and Pradhan (arXiv:1908.00331) explicitly determine automorphism orbits for extraspecial groups with \(|Z|=|G'|=p\), including both exponent types. Their orbit theorems do not cover the present \(|Z|=p^k\) with \(k\ge2\), so the present claim is not a special case of those stated classifications. Camina and collaborators (arXiv:2504.10565) study the weaker equal-order-pair property; an equality of orders alone does not construct the requisite automorphisms. Our argument supplies the explicit higher-center automorphism constructions and the exclusion of all other normal subgroups.

## Limitations

The classification assumes odd \(p\) and cyclic center of order at least \(p^2\). The 2-group case and larger commutator subgroups are not addressed. The result is established by a mathematical proof and independent finite consistency checks but has not undergone independent specialist validation. A preexisting equivalent orbit-theoretic deduction in older or poorly indexed literature cannot be entirely excluded. The relevant 2025 general equal-order paper was inspected in its public full-text arXiv PDF, including its nilpotent-group results; those results identify order-only necessary and sufficient conditions without establishing the claimed automorphism transitivity.

## References

1. R. McCulloch and M. Tărnăuceanu, *Group cosets with all elements automorphically equivalent*, arXiv:2611.11746v1 (2026), https://arxiv.org/abs/2611.11746.
2. A. Kumar and S. K. Pradhan, *On the Endomorphism Semigroups of Extra-special p-groups and Automorphism Orbits*, arXiv:1908.00331 (2019), https://arxiv.org/abs/1908.00331.
3. A. R. Camina, R. D. Camina, M. L. Lewis, E. Pacifici, L. Sanus and M. Vergani, *Group cosets with all elements of equal order*, arXiv:2504.10565 (2025), https://arxiv.org/abs/2504.10565.
