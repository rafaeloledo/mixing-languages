#include <stdio.h>

void hello_world() {
  printf("Hello, World!\n");
}

long sum_numbers(long n) {
  long total = 0;
  for (long i = 0; i < n; i++) {
    total += 1;
  }
  return total;
}
