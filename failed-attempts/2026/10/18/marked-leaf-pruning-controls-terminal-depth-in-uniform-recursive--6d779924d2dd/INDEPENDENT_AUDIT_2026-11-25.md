# Independent mathematical audit

## correctness

PASS

The leaf event restricts each independent parent choice separately, always leaving the root admissible. All surviving parents are uniform on the earlier survivors, and deleting marked leaves removes no vertex of the last-born root path. For the event probability, delete the smallest marked leaf first: its singleton probability is (i_1−1)/(n−1), and since all other marked vertices are later, none could have been its parent. Iteration gives the frozen product. The depth PGF follows from h_k=z/(k−1) times the sum of h_j for j<k (h_1=1), giving the independent Bernoulli convolution in law. The leaf transition preserves the count with probability L_n/n and otherwise increases it by one, giving the Eulerian recurrence. Expanding the product over leaf indicators and grouping subsets by size gives the stated Eulerian factorial moments and hence the joint PGF. For singleton events, summing the leaf probabilities gives (n−2)/2; the Bernoulli convolution then gives the exact transform covariance and strict sign. In a separate finite parent-vector enumeration at n=9 (40,320 trees), the two marked triples {3,5,8} and {2,4,6} had 3,600 and 720 hits, respectively, and f(x)=x² gave covariance −433/160, exactly as predicted; this does not prove the general law. The uploaded verifier was inspected, not run.

## originality

FAIL

The distinct indexed record 4e2828958fad explicitly gives the stronger fixed-leaf erasure theorem and the mixed PGF with every prescribed product of leaf indicators, plus the exact depth–leaf covariance profile. Specializing to the last-born vertex and expanding the standard PGF product yields the frozen joint law and transform formula. The printed Eulerian-derivative form is not verbatim in the comparator, but is a direct extraction. The labels on the two directories do not establish historical priority.

## value

FAIL

The joint distribution of terminal depth and leaves and the exact negative transform covariance are well-motivated invariants of the recursive-tree growth process. The stronger indexed mixed-indicator law already determines them; repackaging it as a PGF with Eulerian coefficients leaves no distinct nonroutine exact fact in this submission.

The dated certificate retains the supplied scientific assessment, sources and limitations.
