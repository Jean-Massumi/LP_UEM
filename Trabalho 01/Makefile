all: main

main: main.o levenshtein.o pocketpy.o
	gcc main.o levenshtein.o pocketpy.o -o main -lm

main.o: main.c levenshtein.h pocketpy.h
	gcc -Wall -c main.c -o main.o

levenshtein.o: levenshtein.c levenshtein.h
	gcc -Wall -c levenshtein.c -o levenshtein.o

pocketpy.o: pocketpy.c pocketpy.h
	gcc -Wall -c pocketpy.c -o pocketpy.o

run: main
	./main

clean:
	rm -f main.o levenshtein.o pocketpy.o main