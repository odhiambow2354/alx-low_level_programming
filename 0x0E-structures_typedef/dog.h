#include <stdio.h>
#ifndef DOG_H
#define DOG_H

/**
 * struct dog - a struct representing a dog
 * @name: the name of the dog
 * @age: the age of the dog
 * @owner: the owner of the dog
 *
 * Description: a struct representing a dog with a name, age, and owner
 */
typedef struct dog
{
char *name;
float age;
char *owner;
} dog_t;

#endif /* DOG_H */

