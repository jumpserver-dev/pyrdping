#include "libpyfreerdp.h"

char pyfreerdpfunc_docs[] = "check rdp connectivity: \n"
"check_connectivity(ip, port, username, password, domain, security)\n"
"ip: string\n"
"port: int\n"
"username: string\n"
"password: string\n"
"domain: string\n"
"security: int (no use )\n"
"return: True: success, False: fail\n"
;

PyMethodDef pyrdping_funcs[] = {
	{	"check_connectivity",
		(PyCFunction)check_connectivity,
		METH_VARARGS,
		pyfreerdpfunc_docs},
	{	NULL}
};

char pyrdpingmod_docs[] = "This is python wrapper for freerdp, it is used to check rdp connectivity";

PyModuleDef pyrdping_mod = {
	PyModuleDef_HEAD_INIT,
	"pyrdping",
	pyrdpingmod_docs,
	-1,
	pyrdping_funcs,
	NULL,
	NULL,
	NULL,
	NULL
};

PyMODINIT_FUNC PyInit_pyrdping(void) {
	return PyModule_Create(&pyrdping_mod);
}
