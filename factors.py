#!/usr/bin/python3

import sys

def factorize(n):
    factors = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            factors.append(i)
            return factors

        def main():
            if len(sys.argv) != 2:
                print("Usage: factors <file>")
                sys.exit(1)

                filename = sys.argv[1]

                with open(filename, 'r') as file:
                    for line in file:
                        try:
                            number = int(line.strip())
                            factors = factorize(number)
                            if factors:
                                smallest_factor = factors[0]
                                largest_factor = factors[-1]
                                print(f"{number}={smallest_factor}*{largest_factor}")
                            else:
                                print(f"{number} is prime.")
                        except ValueError:
                            print(f"Invalid input: {line.strip()}")

                            if __name__ == "__main__":
                                    main()
