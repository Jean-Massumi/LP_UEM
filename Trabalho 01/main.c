#include "pocketpy.h"
#include <stdio.h>
#include "levenshtein.h"

static bool distance(int argc, py_Ref argv) {
  PY_CHECK_ARGC(2);
  PY_CHECK_ARG_TYPE(0, tp_str);
  PY_CHECK_ARG_TYPE(1, tp_str);
  const char *s1 = py_tostr(py_arg(0));
  const char *s2 = py_tostr(py_arg(1));
  py_newint(py_retval(), levenshtein(s1, s2));
  
  return true;
}


int main() {
  py_initialize();

  char conteudo[10000];
  FILE *arquivo = fopen("script.py", "rb");
  int bytes_lidos = fread(conteudo, 1, 10000, arquivo);
  conteudo[bytes_lidos] = '\0';
  fclose(arquivo);

  py_GlobalRef __main__ = py_getmodule("__main__");

  py_bindfunc(__main__, "distance", distance);

  if (!py_exec(conteudo, "", EXEC_MODE, NULL)) {
    py_printexc();
    goto finalize;
  }


finalize:
  py_finalize();
  return 0;
}