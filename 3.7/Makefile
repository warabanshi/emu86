# make for px86

main: main.c 
	gcc -Wall -o px86 main.c instruction.c modrm.c emulator_function.c

code: test.c
	gcc -nostdlib -fno-asynchronous-unwind-tables -g -fno-stack-protector -c test.c
	nasm -f elf64 crt0.asm
	ld --entry=start --oformat=binary -Ttext 0x7c00 -o test.bin crt0.o test.o

clean: clean
	rm -f *.o
	rm -f px86
	rm -f test.bin
	rm -f a.out
