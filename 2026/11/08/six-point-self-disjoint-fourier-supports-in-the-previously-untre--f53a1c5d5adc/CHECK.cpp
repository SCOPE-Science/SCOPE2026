// Exact finite-field certificate for small principal Fourier minors on F_7^2.
// Compile: c++ -O2 -std=c++17 CHECK.cpp -o check && ./check
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <utility>
using i64 = std::int64_t;
constexpr i64 PRIME = 1000000093LL;
constexpr i64 ROOT = 993004909LL;
std::array<i64, 7> powers{};
i64 table[49][49]{};
int selected[5]{};
i64 inspected = 0;
std::array<i64, 6> per_size{};

i64 power(i64 a, i64 exponent) {
    i64 out = 1;
    while (exponent) {
        if (exponent & 1) out = out * a % PRIME;
        a = a * a % PRIME;
        exponent >>= 1;
    }
    return out;
}
void require(bool condition, const char* message) {
    if (!condition) throw std::runtime_error(message);
}
bool nonsingular(int n) {
    i64 matrix[5][5]{};
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            matrix[i][j] = table[selected[i]][selected[j]];
    for (int col = 0; col < n; ++col) {
        int pivot = col;
        while (pivot < n && matrix[pivot][col] == 0) ++pivot;
        if (pivot == n) return false;
        if (pivot != col)
            for (int j = col; j < n; ++j)
                std::swap(matrix[pivot][j], matrix[col][j]);
        i64 inverse = power(matrix[col][col], PRIME - 2);
        for (int row = col + 1; row < n; ++row) {
            i64 factor = matrix[row][col] * inverse % PRIME;
            for (int j = col + 1; j < n; ++j)
                matrix[row][j] = (matrix[row][j] - factor * matrix[col][j] % PRIME + PRIME) % PRIME;
            matrix[row][col] = 0;
        }
    }
    return true;
}
void inspect(int size, int pos, int next) {
    if (pos == size) {
        ++inspected;
        ++per_size[size];
        if (!nonsingular(size)) {
            std::cerr << "Singular principal set of size " << size << ':';
            for (int j = 0; j < size; ++j) std::cerr << ' ' << selected[j];
            std::cerr << '\n';
            throw std::runtime_error("Nonzero-minor certificate FAILED");
        }
        return;
    }
    for (int idx = next; idx <= 49 - (size - pos); ++idx) {
        selected[pos] = idx;
        inspect(size, pos + 1, idx + 1);
    }
}
int main() {
    try {
        for (i64 d = 2; d * d <= PRIME; ++d)
            require(PRIME % d != 0, "Coefficient field modulus is not prime");
        powers[0] = 1;
        for (int e = 1; e < 7; ++e) powers[e] = powers[e - 1] * ROOT % PRIME;
        require(powers[6] * ROOT % PRIME == 1, "Root has wrong order");
        for (int e = 1; e < 7; ++e) require(powers[e] != 1, "Root not primitive");
        for (int row = 0; row < 49; ++row)
            for (int col = 0; col < 49; ++col) {
                int exponent = ((row / 7) * (col / 7) + (row % 7) * (col % 7)) % 7;
                table[row][col] = powers[exponent];
            }
        // Direct check of the six-site witness for p=7 and t=2.
        int sites[6] = {0, 1, 2, 15, 16, 17};
        i64 omega = powers[1], omega2 = powers[2], omega3 = powers[3];
        i64 coeff[6] = {(PRIME - omega3) % PRIME, (omega + omega2) % PRIME,
                         PRIME - 1, omega3,
                         (PRIME - (omega + omega2) % PRIME) % PRIME, 1};
        for (int i = 0; i < 6; ++i) {
            require(coeff[i] != 0, "Witness is not six-supported");
            i64 sum = 0;
            for (int j = 0; j < 6; ++j)
                sum = (sum + table[sites[i]][sites[j]] * coeff[j]) % PRIME;
            require(sum == 0, "Six-point witness failed");
        }
        selected[0] = 0;
        const i64 expected[6] = {0, 1, 48, 1128, 17296, 194580};
        for (int k = 1; k <= 5; ++k) {
            inspect(k, 1, 1);
            require(per_size[k] == expected[k], "Enumeration did not cover all subsets");
            std::cout << "k=" << k << " nonsingular=" << per_size[k] << '\n';
        }
        require(inspected == 213053, "Incorrect total certificate size");
        std::cout << "CHECK_OK exact_principal_minors=" << inspected
                  << " prime=" << PRIME << " primitive_root=" << ROOT << '\n';
    } catch (const std::exception& e) {
        std::cerr << "CHECK_FAILED " << e.what() << '\n';
        return 1;
    }
}
