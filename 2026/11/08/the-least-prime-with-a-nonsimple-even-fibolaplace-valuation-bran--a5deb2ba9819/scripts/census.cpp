#include <cassert>
#include <iostream>
#include <vector>
#include <utility>

// Exhaustive exact finite-field census for the even FiboLaplace polynomial.
// All products and sums are reduced modulo the current prime at each step.
int main() {
    constexpr int limit = 971;
    std::vector<bool> prime(limit + 1, true);
    prime[0] = prime[1] = false;
    for (int d = 2; d * d <= limit; ++d) {
        if (prime[d]) {
            for (int n = d * d; n <= limit; n += d) prime[n] = false;
        }
    }
    int tested = 0, roots = 0, below = 0, repeated = 0;
    long long steps = 0;
    for (int p = 3; p <= limit; p += 2) {
        if (!prime[p]) continue;
        ++tested;
        std::vector<int> at_p, at_p_multiple;
        for (int a = 1; a < p; ++a) {
            long long product = 1, derivative_product = 0;
            long long second_product = 0, total = 1, derivative = 0, second = 0;
            for (int k = 1; k < p; ++k) {
                long long factor = (1LL * a * a - 1LL * k * k) % p;
                if (factor < 0) factor += p;
                long long new_second = (second_product * factor
                       + 4LL * a * derivative_product + 2LL * product) % p;
                long long new_derivative = (derivative_product * factor
                       + 2LL * a * product) % p;
                product = (product * factor) % p;
                derivative_product = new_derivative;
                second_product = new_second;
                total = (total + product) % p;
                derivative = (derivative + derivative_product) % p;
                second = (second + second_product) % p;
                ++steps;
            }
            if (total == 0) {
                ++roots;
                at_p.push_back(a);
                if (p < limit) ++below;
                if (derivative == 0) {
                    ++repeated;
                    at_p_multiple.push_back(a);
                    assert(p == 971 && (a == 194 || a == 777));
                    assert(second == 471);
                    std::cout << "REPEATED p=" << p << " a=" << a
                              << " second=" << second << '\n';
                }
            }
        }
        if (p < 971) assert(at_p_multiple.empty());
        if (p == 971) {
            assert((at_p == std::vector<int>{194, 777}));
            assert(at_p_multiple == at_p);
        }
    }
    assert(tested == 163 && roots == 144 && below == 142 && repeated == 2);
    // Recurrence provides independent valuation-one checks at both roots.
    constexpr long long modulus = 971LL * 971LL;
    long long last_two = 1, last_one = 1;
    for (int n = 3; n <= 1554; ++n) {
        long long next = ((n - 1LL) * last_one - last_two
                          + 1 - ((n & 1) ? -1 : 1)) % modulus;
        if (next < 0) next += modulus;
        last_two = last_one;
        last_one = next;
        if (n == 388 || n == 1554) {
            assert(next != 0 && next % 971 == 0);
            assert(next == (n == 388 ? 473848 : 468993));
            std::cout << "VALUATION_ONE n=" << n << " e_mod_p2=" << next << '\n';
        }
    }
    std::cout << "PRIMES " << tested << " ROOTS " << roots
              << " ROOTS_BELOW_971 " << below << " REPEATED " << repeated
              << " PRODUCT_STEPS " << steps << '\n';
    std::cout << "EXHAUSTIVE_CENSUS_OK\n";
}
