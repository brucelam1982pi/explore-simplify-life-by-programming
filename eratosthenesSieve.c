/* gcc eratosthenesSieve.c -o eratosthenesSieve
   ./eratosthenesSieve
   time ./eratosthenesSieve

9999971
9999973
9999991
Total of prime numbers less than 10000000 is : 664579

real	0m3.552s
user	0m1.009s
sys	0m1.988s

time primesieve 10000000 --print | head

9999971
9999973
9999991

real	0m1.424s
user	0m0.088s
sys	0m0.476s

N = 100000000;
time ./eratosthenesSieve
99999941
99999959
99999971
99999989
Total of prime numbers less than 100000000 is : 5761455

real	0m33.127s
user	0m9.484s
sys	0m17.120s
*/

#include <stdio.h>
#include <stdlib.h>

/* N: positive integer
   verbose: 1 -- print all prime numbers < N, 0 -- no print
   return total number of prime numbers < N. 
   return -1 when there is not enough memory.
*/
int eratosthenesSieve(unsigned long long int N, int verbose) {
  // prime numbers are positive, better to use largest unsiged integer
  unsigned long long int i, j, total; // total: number of prime numbers < N
  _Bool *a = malloc(sizeof(_Bool) * N);

  if (a == NULL) {
    printf("No enough memory.\n");
    return -1;
  }
  
  /* a[i] equals 1: i is prime number.
     a[i] equals 0: i is not prime number.
     From beginning, set i as prime number. Later filter out non-prime numbers
  */
  for (i = 2; i < N; i++) {
    a[i] = 1; 
  }

  // mark multiples(<N) of i as non-prime numbers
  for (i = 2; i < N; i++) {
    if (a[i]) { // a[i] is prime number at this point
      for (j = i; j < (N / i) + 1; j++) {
	/* Thanks Richard Stallman's advice for correct description.
           mark all multiple of 2 * 2, 2 * 3, as non-prime numbers;
	   do the same for 3,4,5,... 2*3 is filter out when i is 2
	   so when i is 3, we only start at 3 * 3
	*/
	a[i * j] = 0;
      }
    }
  }

  // count total. print prime numbers < N if needed.
  total = 0;
  for (i = 2; i < N; i++) {
    if (a[i]) { // i is prime number
      if (verbose) {
	printf("%llu\n", i);
      }
      total += 1;
    }
  }

  free(a);
  return total;
}

int main() {
  unsigned long long int a1 = 0, a2 = 0, N = 100000000;
  
  a1 = eratosthenesSieve(N, 1); // print the prime numbers
  printf("Total of prime numbers less than %llu is : %llu\n", N, a1);
  /*
  a2 = eratosthenesSieve(N, 0); // not print the prime numbers
  printf("Total of prime numbers less than %llu is : %llu\n", N, a2);
  */
  return 0;
}

/*
#   This is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This bash script is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   See <http://www.gnu.org/licenses/> for GNU General Public License.
#
#   contact author: brucelam1982pi@gmail.com Bruce
*/
