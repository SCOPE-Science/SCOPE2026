# Exact binary four-variable conditional-independence census and sharp ten-world bound

## Finding
Let \(T\) range over the nonempty teams of four named Boolean variables. Record, for each pair of distinct variables and each subset of the other two variables, whether the corresponding conditional-independence atom holds in the relational sense of team semantics. There are exactly **\(1{,}342\)** distinct complete elementary conditional-independence profiles. Under permutations of the four variable names they form exactly **\(125\)** isomorphism classes. Every profile has a witnessing team of at most **\(10\)** assignments, and this universal bound is sharp: exactly **\(28\)** profiles, comprising **\(4\)** variable-renaming classes, have minimum witness size \(10\).

This is a complete classification for four **Boolean** variables and the specified \(24\) atomic sentences; it does not assert that the same bound holds for richer variable domains or for formulas built using Boolean connectives.

## Assumptions and scope
Use the fixed assignment space \(\Omega=\{0,1\}^4\), where assignments are integers from \(0\) to \(15\) in binary, with variable \(x_i\) represented by bit \(i\), for \(i\in\{0,1,2,3\}\). A team \(T\) is a **nonempty subset** of \(\Omega\), so there are \(2^{16}-1=65{,}535\) teams. No duplicate rows or probabilities are part of the semantics. Equivalently, an ordinary finite world model with four Boolean predicates may be reduced to its set of distinct valuations: collapsing worlds with identical four-bit assignments preserves all of the listed atomic truths. Consequently the least team cardinality is also the least number of worlds necessary for a model of the same complete atomic profile.

For every \(0\le i<j<4\) and every conditioning set \(Z\subseteq\{0,1,2,3\}\setminus\{i,j\}\), define the atomic statement \(x_i\perp_{x_Z}x_j\) to hold in \(T\) exactly when
\[
\forall s,t\in T\ \bigl(s|_Z=t|_Z\implies \exists u\in T:\ u|_Z=s|_Z,\ u_i=s_i,\ u_j=t_j\bigr).
\]
There are \(\binom42\cdot2^2=24\) such atoms. The *profile* is their complete \(24\)-bit truth vector, with atoms ordered first by \(i\), then by \(j\), then by increasing integer bit mask of \(Z\). Two teams have the same complete elementary theory precisely when these vectors agree. The group of variable-name permutations \(S_4\) acts on profiles by permuting all indices and conditioning sets.

For data files, the assignment team itself is encoded by a \(16\)-bit integer, with bit \(s\) indicating membership of assignment \(s\). Hexadecimal identifiers in the CSV files are fixed-width base-16 encodings, not mathematical exponent expressions.

## Proof
**1. Exact rectangularity criterion.** Fix an atom \(x_i\perp_{x_Z}x_j\) and a conditioning value \(z\) realized by a member of \(T\). The four possible ordered value pairs \((s_i,s_j)\in\{0,1\}^2\) occupy a set \(P_z\) of cells of a \(2\times2\) matrix. The defining existential clause holds exactly if \(P_z=\pi_i(P_z)\times\pi_j(P_z)\): each combination of a realized first and realized second coordinate has a realizing assignment in the same conditioning fibre. Because there are just four cells, this fails exactly when the two-cell support is one of the two diagonals, or when exactly three cells occur. In the chosen pair-index ordering the forbidden bit patterns are \(6\), \(9\), and the four three-bit patterns. This is an elementary exhaustive classification of all \(16\) possible fibre supports, not a heuristic.

**2. Exhausting the complete universe.** Each nonempty team is represented uniquely by an integer \(t\) with \(1\le t<2^{16}\). The accompanying standard-C++ checker iterates over this exact finite interval and over all \(24\) independently generated atoms. Each atom is evaluated once using the rectangularity characterization from Step 1 and once using literal nested universal/existential loops implementing the definition above. The two algorithms agree in each of exactly \(65{,}535\times24=1{,}572{,}840\) tests. This establishes that the \(24\)-bit signatures stored for all teams are exactly their semantic truth vectors.

The checker groups the signatures by exact equality and retains both the total number of realizing teams and the least size of any realizing team. Direct grouping yields \(1{,}342\) signatures. The distribution of signatures by minimum team size \(r\) is

| \(r\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Profiles | 1 | 11 | 29 | 114 | 264 | 397 | 307 | 129 | 62 | 28 |

These entries sum to \(1{,}342\). Every one of the \(65{,}535\) teams is accounted for in the per-profile frequencies. In particular, all profiles have a witness of size at most \(10\), while at least one requires \(10\); therefore the cutoff is sharp.

**3. Variable-renaming classes.** For each of the \(24\) permutations of \(\{0,1,2,3\}\), the checker independently transports the ordered triple \((i,j,Z)\) for every true atom, reorders the pair, and looks up the new position in the list of \(24\) atoms. It checks that the transformed signature belongs to the enumerated set and that all signatures within a resulting orbit have the same least witness size. The orbit calculation yields \(125\) orbits, with the following distribution by orbit size: \(5\) orbits of size \(1\), \(7\) of size \(3\), \(14\) of size \(4\), \(22\) of size \(6\), \(60\) of size \(12\), and \(17\) of size \(24\). The weighted sum is \(5+21+56+132+720+408=1{,}342\).

The orbit minimum-witness-size distribution, for the sizes \(1\) through \(10\), is respectively \(1,3,5,15,24,31,22,14,6,4\). Thus the \(28\) ten-world profiles form precisely \(4\) orbits, represented by the following exact canonical profile and witness team encodings:

| Canonical profile (hex) | Variable-renaming orbit size | Ten-assignment team (hex) |
| --- | ---: | --- |
| `05f5f3` | 12 | `06ff` |
| `077777` | 6 | `0ff6` |
| `11b1bb` | 4 | `18ff` |
| `13333f` | 6 | `1ff1` |

The first witness team contains assignments \(0,1,2,3,4,5,6,7,9,10\); no team of at most nine assignments realizes its complete \(24\)-atom signature, as certified by the same exhaustive enumeration. This concludes the classification.

## Verification
The artifact `checker.cpp` is self-contained C++17 source; no external library or database is required. From the directory containing the provided files, run `g++ -std=c++17 -O2 -Wall -Wextra -pedantic checker.cpp -o checker`, followed by `./checker --tables`. This checks the semantics twice per team/atom pair; checks the asserted number of profiles, orbit structure, minimum-size distributions, and sharp witness; and reproduces `profiles.csv` and `orbits.csv` byte-for-byte.

`profiles.csv` has one record for each labelled profile: signature, minimum assignments, number of teams with that signature, and one least-size team. `orbits.csv` has one record for each naming orbit: canonical signature, orbit size, minimum assignments and one matching witness team. The checker emits the sentinel `TEAM_CI4_EXHAUSTIVE_OK` upon completing its assertions. This is an exhaustive **finite** certificate, not a claim of independent human verification or a theorem about unbounded variable counts.

## Relationship to prior work
Grädel and Väänänen introduced the team-semantics independence atom in *Dependence and Independence* (2011 preprint; arXiv version 2012), whose defining clause is the semantics used here. Šimeček's *A Short Note on Discrete Representability of Independence Models* (2006) concerns **probabilistic** conditional-independence structures of four variables, generally allowing arbitrary discrete state spaces and distributions; its four-variable counts are not a binary-support team profile census. Barbero, Girlando, Müller and Yang's *Labelled Sequent Calculi for Propositional Team Logics*, first publicly posted June 30, 2026, develops proof theory for finite-atom team logics but does not furnish these exact finite enumeration data in the accessible material. The present result specifies both the domain restriction and the exact \(24\)-atom signature so that differences of semantics cannot be hidden behind similar terminology.

## Limitations
The calculations are exhaustive only because \(\Omega\) has \(16\) assignments. They do not classify independence atoms involving multi-variable tuples on either side, arbitrary Boolean combinations of atoms, non-Boolean domains, or probabilistic conditional independence. The truth of the exact count depends on the supplied executable finite derivation, whose two distinct semantic implementations are compared; the code is short enough for independent manual inspection, but such independent audit has not occurred. Exhaustive searching and targeted comparisons have not ruled out equivalent results in unindexed or inaccessible specialist literature.

## References
- F. Barbero, M. Girlando, V. Müller and F. Yang, *Labelled Sequent Calculi for Propositional Team Logics*, arXiv:2606.31860 (first posted 2026-06-30), https://arxiv.org/abs/2606.31860.
- E. Grädel and J. Väänänen, *Dependence and Independence*, ILLC preprint PP-2011-07 and arXiv:1208.5268, https://arxiv.org/abs/1208.5268.
- P. Šimeček, *A Short Note on Discrete Representability of Independence Models*, Third European Workshop on Probabilistic Graphical Models (2006), https://www.researchgate.net/publication/289965351_A_short_note_on_discrete_representability_of_independence_models.
- S. Abramsky, J. Puljujärvi and J. Väänänen, *Team Semantics and Independence Notions in Quantum Physics*, arXiv:2107.10817, https://arxiv.org/abs/2107.10817.
