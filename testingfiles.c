#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

//COLORES
#define RED "\033[31m"
#define BOLD  "\033[1m"
#define OFF   "\e[m"
#define GREEN "\033[32m"
#define YELLOW "\033[33m"
#define CYAN "\033[34m"
#define PINK "\033[35m"
#define BLUE "\033[36m"

int getwordsize(char text[],int position,int cap){
  int wordsize, i; wordsize = 0; i = position;
  for ( i = position; (text[i] != ' ' && text[i] != 10 && ((text[i] >64 && text[i] <91)||(text[i] >96 && text[i] <123)) && i < cap); i++){
    wordsize +=1;
  }
  return wordsize;
}


int main(){
  setlocale(LC_ALL, "Portuguese_Brazil.UTF-8");
  char input; input = ' ';
  int n = 0;
  char *text = NULL;
  char *moretext = NULL;
  int sizetext, conditions, mai; conditions = 0; mai = 1;

  while (input != '`'){
    scanf("%c",&input);
    n++;

    moretext = (char*) realloc(text,n * sizeof(char));

    if (moretext != NULL){
      text = moretext;
      text[n-1] = input;
    }
    else{
      free(text);
      puts("Error:(");
      exit(1);
    }
  }

  for (int i = 0; i < n; i++)
  {
    
    if ((text[i] > 64 && text[i]<91)|| (text[i] > 96 && text[i] < 123) )
    {
    
    
      if (mai)
      {
        if ((text[i] > 96 && text[i] < 123))
        {
          printf(YELLOW"%c"OFF,text[i]-32);
        }
        else{
          printf(YELLOW"%c"OFF,text[i]);
        }
        conditions -=1;
        mai -=1;
        
      }
    
      else if (conditions > 0)
      {
        printf(YELLOW"%c"OFF,text[i]);
        conditions -= 1;
      }
      else{
        printf("%c",text[i]);
      }
    }
    else{
      printf(CYAN"%c"OFF,text[i]);
    }
    
    if (text[i] == ' ' || text[i] == 10)
    {
      conditions = (getwordsize(text,i+1,n))/2;
      mai = 1;
    }

  }
  return 0;
}