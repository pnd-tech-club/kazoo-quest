// Generated code for Python source for module 'Loadingbar'
// created by Nuitka version 0.5.13.1

// This code is in part copyright 2015 Kay Hayen.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "nuitka/prelude.hpp"

#include "__helpers.hpp"

// The _module_Loadingbar is a Python object pointer of module type.

// Note: For full compatibility with CPython, every module variable access
// needs to go through it except for cases where the module cannot possibly
// have changed in the mean time.

PyObject *module_Loadingbar;
PyDictObject *moduledict_Loadingbar;

// The module constants used
extern PyObject *const_str_plain_cyan;
extern PyObject *const_str_plain_write;
extern PyObject *const_str_plain_Loadingbar;
extern PyObject *const_int_pos_120;
extern PyObject *const_int_neg_1;
static PyObject *const_int_pos_290;
extern PyObject *const_str_plain_clear;
extern PyObject *const_str_plain_cols;
extern PyObject *const_str_plain_join;
extern PyObject *const_str_plain_color;
extern PyObject *const_dict_c008e769f7ad26f5db2cafc17e3e1194;
extern PyObject *const_int_pos_30;
extern PyObject *const_tuple_empty;
extern PyObject *const_str_plain_os;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain_sys;
extern PyObject *const_int_0;
static PyObject *const_str_digest_137c0bc657f171dfd78596f46e2c2392;
static PyObject *const_str_chr_13;
static PyObject *const_str_plain_print;
static PyObject *const_int_pos_6000;
extern PyObject *const_str_plain___file__;
extern PyObject *const_str_plain_system;
extern PyObject *const_str_plain_kazooquest;
static PyObject *const_str_plain_extend;
extern PyObject *const_str_digest_e473a28e1148a90d05cc0fa2ed8c576c;
static PyObject *const_str_digest_97cd7ee5ecd74de7e4c58cd208794b8c;
extern PyObject *const_str_plain_rows;
extern PyObject *const_int_pos_1;
extern PyObject *const_str_empty;
extern PyObject *const_str_plain_stdout;
static PyObject *const_str_plain_end;
extern PyObject *const_str_plain_off;
extern PyObject *const_str_newline;
extern PyObject *const_str_plain_wait;
static PyObject *const_str_plain_desu;
static PyObject *const_str_digest_6a33f9277a8dde64e990655418d6695e;
extern PyObject *const_str_plain_yellow;
static PyObject *const_str_plain_print_function;
extern PyObject *const_str_plain_format;
static PyObject *const_dict_a0adbc06b00682b62dab9d9190a1ebe9;
extern PyObject *const_dict_283dacd4984ab69b6cfcca3a8f5e15e1;
static PyObject *module_filename_obj;

static void _initModuleConstants( void )
{
    const_int_pos_290 = PyInt_FromLong( 290l );
    const_str_digest_137c0bc657f171dfd78596f46e2c2392 = UNSTREAM_STRING( &constant_bin[ 2309 ], 3, 0 );
    const_str_chr_13 = UNSTREAM_CHAR( 13, 0 );
    const_str_plain_print = UNSTREAM_STRING( &constant_bin[ 2312 ], 5, 1 );
    const_int_pos_6000 = PyInt_FromLong( 6000l );
    const_str_plain_extend = UNSTREAM_STRING( &constant_bin[ 2317 ], 6, 1 );
    const_str_digest_97cd7ee5ecd74de7e4c58cd208794b8c = UNSTREAM_STRING( &constant_bin[ 2323 ], 112, 0 );
    const_str_plain_end = UNSTREAM_STRING( &constant_bin[ 2320 ], 3, 1 );
    const_str_plain_desu = UNSTREAM_STRING( &constant_bin[ 82 ], 4, 1 );
    const_str_digest_6a33f9277a8dde64e990655418d6695e = UNSTREAM_STRING( &constant_bin[ 2435 ], 50, 0 );
    const_str_plain_print_function = UNSTREAM_STRING( &constant_bin[ 2485 ], 14, 1 );
    const_dict_a0adbc06b00682b62dab9d9190a1ebe9 = _PyDict_NewPresized( 1 );
    PyDict_SetItem( const_dict_a0adbc06b00682b62dab9d9190a1ebe9, const_str_plain_end, const_str_chr_13 );
    assert( PyDict_Size( const_dict_a0adbc06b00682b62dab9d9190a1ebe9 ) == 1 );
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_Loadingbar( void )
{

}
#endif

// The module code objects.
static PyCodeObject *codeobj_2722d1a92f02c10d7f6d60015b6e3f71;

static void _initModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_6a33f9277a8dde64e990655418d6695e );
    codeobj_2722d1a92f02c10d7f6d60015b6e3f71 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_Loadingbar, 0, const_tuple_empty, 0, CO_NOFREE | CO_FUTURE_PRINT_FUNCTION );
}

// The module function declarations.


// The module function definitions.



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_Loadingbar =
{
    PyModuleDef_HEAD_INIT,
    "Loadingbar",   /* m_name */
    NULL,                /* m_doc */
    -1,                  /* m_size */
    NULL,                /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
  };
#endif

#define _MODULE_UNFREEZER 0

#if _MODULE_UNFREEZER

#include "nuitka/unfreezing.hpp"

// Table for lookup to find "frozen" modules or DLLs, i.e. the ones included in
// or along this binary.

static struct Nuitka_MetaPathBasedLoaderEntry meta_path_loader_entries[] =
{

    { NULL, NULL, 0 }
};

#endif

// The exported interface to CPython. On import of the module, this function
// gets called. It has to have an exact function name, in cases it's a shared
// library export. This is hidden behind the MOD_INIT_DECL.

MOD_INIT_DECL( Loadingbar )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_Loadingbar );
    }
    else
    {
        _init_done = true;
    }
#endif

#ifdef _NUITKA_MODULE
    // In case of a stand alone extension module, need to call initialization
    // the init here because that's the first and only time we are going to get
    // called here.

    // Initialize the constant values used.
    _initBuiltinModule();
    createGlobalConstants();

    // Initialize the compiled types of Nuitka.
    PyType_Ready( &Nuitka_Generator_Type );
    PyType_Ready( &Nuitka_Function_Type );
    PyType_Ready( &Nuitka_Method_Type );
    PyType_Ready( &Nuitka_Frame_Type );
#if PYTHON_VERSION < 300
    _initSlotCompare();
#endif
#if PYTHON_VERSION >= 270
    _initSlotIternext();
#endif

    patchBuiltinModule();
    patchTypeComparison();

#endif

#if _MODULE_UNFREEZER
    registerMetaPathBasedUnfreezer( meta_path_loader_entries );
#endif

    _initModuleConstants();
    _initModuleCodeObjects();

    // puts( "in initLoadingbar" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_Loadingbar = Py_InitModule4(
        "Loadingbar",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_Loadingbar = PyModule_Create( &mdef_Loadingbar );
#endif

    moduledict_Loadingbar = (PyDictObject *)((PyModuleObject *)module_Loadingbar)->md_dict;

    CHECK_OBJECT( module_Loadingbar );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_plain_Loadingbar, module_Loadingbar );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_Loadingbar );

    if ( PyDict_GetItem( module_dict, const_str_plain___builtins__ ) == NULL )
    {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then.
#if !defined(_NUITKA_EXE) || !0
        value = PyModule_GetDict( value );
#endif

#ifndef __NUITKA_NO_ASSERT__
        int res =
#endif
            PyDict_SetItem( module_dict, const_str_plain___builtins__, value );

        assert( res == 0 );
    }

#if PYTHON_VERSION >= 330
#if _MODULE_UNFREEZER
    PyDict_SetItem( module_dict, const_str_plain___loader__, metapath_based_loader );
#else
    PyDict_SetItem( module_dict, const_str_plain___loader__, Py_None );
#endif
#endif

    // Temp variables if any
    PyObject *exception_type, *exception_value;
    PyTracebackObject *exception_tb;
    PyObject *tmp_args_element_name_1;
    PyObject *tmp_args_element_name_2;
    PyObject *tmp_args_name_1;
    PyObject *tmp_args_name_2;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_assign_source_4;
    PyObject *tmp_assign_source_5;
    PyObject *tmp_assign_source_6;
    PyObject *tmp_assign_source_7;
    PyObject *tmp_assign_source_8;
    PyObject *tmp_assign_source_9;
    PyObject *tmp_assign_source_10;
    PyObject *tmp_assign_source_11;
    PyObject *tmp_call_arg_element_1;
    PyObject *tmp_call_arg_element_2;
    PyObject *tmp_call_arg_element_3;
    PyObject *tmp_call_arg_element_4;
    PyObject *tmp_called_name_1;
    PyObject *tmp_called_name_2;
    PyObject *tmp_called_name_3;
    PyObject *tmp_called_name_4;
    PyObject *tmp_called_name_5;
    PyObject *tmp_called_name_6;
    PyObject *tmp_called_name_7;
    PyObject *tmp_called_name_8;
    PyObject *tmp_called_name_9;
    int tmp_cmp_GtE_1;
    int tmp_cmp_Lt_1;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_left_2;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_compare_right_2;
    PyObject *tmp_dict_key_1;
    PyObject *tmp_dict_value_1;
    PyObject *tmp_import_globals_1;
    PyObject *tmp_import_globals_2;
    PyObject *tmp_import_globals_3;
    PyObject *tmp_kw_name_1;
    PyObject *tmp_kw_name_2;
    PyObject *tmp_kw_name_3;
    PyObject *tmp_left_name_1;
    PyObject *tmp_left_name_2;
    PyObject *tmp_left_name_3;
    PyObject *tmp_left_name_4;
    PyObject *tmp_left_name_5;
    PyObject *tmp_len_arg_1;
    PyObject *tmp_right_name_1;
    PyObject *tmp_right_name_2;
    PyObject *tmp_right_name_3;
    PyObject *tmp_right_name_4;
    PyObject *tmp_right_name_5;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    PyObject *tmp_source_name_3;
    PyObject *tmp_source_name_4;
    PyObject *tmp_source_name_5;
    PyObject *tmp_source_name_6;
    PyObject *tmp_source_name_7;
    PyObject *tmp_subscribed_name_1;
    PyObject *tmp_subscribed_name_2;
    PyObject *tmp_subscribed_name_3;
    PyObject *tmp_subscribed_name_4;
    PyObject *tmp_subscript_name_1;
    PyObject *tmp_subscript_name_2;
    PyObject *tmp_subscript_name_3;
    PyObject *tmp_subscript_name_4;
    PyObject *tmp_tuple_element_1;
    PyObject *tmp_tuple_element_2;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    PyFrameObject *frame_module;


    // Module code.
    tmp_assign_source_1 = Py_None;
    UPDATE_STRING_DICT0( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = const_str_digest_6a33f9277a8dde64e990655418d6695e;
    UPDATE_STRING_DICT0( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    tmp_assign_source_3 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "print_function");
    UPDATE_STRING_DICT0( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_print_function, tmp_assign_source_3 );
    // Frame without reuse.
    frame_module = MAKE_FRAME( codeobj_2722d1a92f02c10d7f6d60015b6e3f71, module_Loadingbar );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_module );
    assert( Py_REFCNT( frame_module ) == 1 );

#if PYTHON_VERSION >= 340
    frame_module->f_executing += 1;
#endif

    // Framed code:
    tmp_import_globals_1 = ((PyModuleObject *)module_Loadingbar)->md_dict;
    frame_module->f_lineno = 3;
    tmp_assign_source_4 = IMPORT_MODULE( const_str_plain_sys, tmp_import_globals_1, tmp_import_globals_1, Py_None, const_int_neg_1 );
    if ( tmp_assign_source_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 3;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_sys, tmp_assign_source_4 );
    tmp_import_globals_2 = ((PyModuleObject *)module_Loadingbar)->md_dict;
    frame_module->f_lineno = 3;
    tmp_assign_source_5 = IMPORT_MODULE( const_str_plain_os, tmp_import_globals_2, tmp_import_globals_2, Py_None, const_int_neg_1 );
    if ( tmp_assign_source_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 3;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_os, tmp_assign_source_5 );
    tmp_source_name_2 = GET_STRING_DICT_VALUE( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_sys );

    if (unlikely( tmp_source_name_2 == NULL ))
    {
        tmp_source_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_sys );
    }

    if ( tmp_source_name_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 0 ], 25, 0 );
        exception_tb = NULL;

        frame_module->f_lineno = 4;
        goto frame_exception_exit_1;
    }

    tmp_source_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_stdout );
    if ( tmp_source_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 4;
        goto frame_exception_exit_1;
    }
    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_write );
    Py_DECREF( tmp_source_name_1 );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 4;
        goto frame_exception_exit_1;
    }
    tmp_source_name_3 = const_str_digest_e473a28e1148a90d05cc0fa2ed8c576c;
    tmp_called_name_2 = LOOKUP_ATTRIBUTE( tmp_source_name_3, const_str_plain_format );
    if ( tmp_called_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_1 );

        frame_module->f_lineno = 4;
        goto frame_exception_exit_1;
    }
    tmp_kw_name_1 = PyDict_Copy( const_dict_283dacd4984ab69b6cfcca3a8f5e15e1 );
    frame_module->f_lineno = 4;
    tmp_args_element_name_1 = CALL_FUNCTION_WITH_KEYARGS( tmp_called_name_2, tmp_kw_name_1 );
    Py_DECREF( tmp_called_name_2 );
    Py_DECREF( tmp_kw_name_1 );
    if ( tmp_args_element_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_called_name_1 );

        frame_module->f_lineno = 4;
        goto frame_exception_exit_1;
    }
    frame_module->f_lineno = 4;
    tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, tmp_args_element_name_1 );
    Py_DECREF( tmp_called_name_1 );
    Py_DECREF( tmp_args_element_name_1 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 4;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_source_name_4 = GET_STRING_DICT_VALUE( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_os );

    if (unlikely( tmp_source_name_4 == NULL ))
    {
        tmp_source_name_4 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_os );
    }

    if ( tmp_source_name_4 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 25 ], 24, 0 );
        exception_tb = NULL;

        frame_module->f_lineno = 5;
        goto frame_exception_exit_1;
    }

    tmp_called_name_3 = LOOKUP_ATTRIBUTE( tmp_source_name_4, const_str_plain_system );
    if ( tmp_called_name_3 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 5;
        goto frame_exception_exit_1;
    }
    tmp_call_arg_element_1 = const_str_plain_clear;
    frame_module->f_lineno = 5;
    tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_3, tmp_call_arg_element_1 );
    Py_DECREF( tmp_called_name_3 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 5;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_assign_source_6 = PyList_New( 0 );
    UPDATE_STRING_DICT1( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_desu, tmp_assign_source_6 );
    tmp_assign_source_7 = PyDict_Copy( const_dict_c008e769f7ad26f5db2cafc17e3e1194 );
    UPDATE_STRING_DICT1( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_color, tmp_assign_source_7 );
    tmp_assign_source_8 = const_int_0;
    UPDATE_STRING_DICT0( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_wait, tmp_assign_source_8 );
    tmp_source_name_5 = GET_STRING_DICT_VALUE( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_os );

    if (unlikely( tmp_source_name_5 == NULL ))
    {
        tmp_source_name_5 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_os );
    }

    if ( tmp_source_name_5 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 25 ], 24, 0 );
        exception_tb = NULL;

        frame_module->f_lineno = 29;
        goto frame_exception_exit_1;
    }

    tmp_called_name_4 = LOOKUP_ATTRIBUTE( tmp_source_name_5, const_str_plain_system );
    if ( tmp_called_name_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 29;
        goto frame_exception_exit_1;
    }
    tmp_call_arg_element_2 = const_str_plain_clear;
    frame_module->f_lineno = 29;
    tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_4, tmp_call_arg_element_2 );
    Py_DECREF( tmp_called_name_4 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 29;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_called_name_5 = LOOKUP_BUILTIN( const_str_plain_print );
    if ( tmp_called_name_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_args_name_1 = PyTuple_New( 1 );
    tmp_subscribed_name_1 = GET_STRING_DICT_VALUE( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_color );

    if (unlikely( tmp_subscribed_name_1 == NULL ))
    {
        tmp_subscribed_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_color );
    }

    if ( tmp_subscribed_name_1 == NULL )
    {
        Py_DECREF( tmp_args_name_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 49 ], 27, 0 );
        exception_tb = NULL;

        frame_module->f_lineno = 30;
        goto frame_exception_exit_1;
    }

    tmp_subscript_name_1 = const_str_plain_yellow;
    tmp_left_name_2 = LOOKUP_SUBSCRIPT( tmp_subscribed_name_1, tmp_subscript_name_1 );
    if ( tmp_left_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_args_name_1 );

        frame_module->f_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_right_name_1 = const_str_digest_97cd7ee5ecd74de7e4c58cd208794b8c;
    tmp_left_name_1 = BINARY_OPERATION_ADD( tmp_left_name_2, tmp_right_name_1 );
    Py_DECREF( tmp_left_name_2 );
    if ( tmp_left_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_args_name_1 );

        frame_module->f_lineno = 30;
        goto frame_exception_exit_1;
    }
    tmp_subscribed_name_2 = GET_STRING_DICT_VALUE( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_color );

    if (unlikely( tmp_subscribed_name_2 == NULL ))
    {
        tmp_subscribed_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_color );
    }

    if ( tmp_subscribed_name_2 == NULL )
    {
        Py_DECREF( tmp_args_name_1 );
        Py_DECREF( tmp_left_name_1 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 49 ], 27, 0 );
        exception_tb = NULL;

        frame_module->f_lineno = 32;
        goto frame_exception_exit_1;
    }

    tmp_subscript_name_2 = const_str_plain_off;
    tmp_right_name_2 = LOOKUP_SUBSCRIPT( tmp_subscribed_name_2, tmp_subscript_name_2 );
    if ( tmp_right_name_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_args_name_1 );
        Py_DECREF( tmp_left_name_1 );

        frame_module->f_lineno = 32;
        goto frame_exception_exit_1;
    }
    tmp_tuple_element_1 = BINARY_OPERATION_ADD( tmp_left_name_1, tmp_right_name_2 );
    Py_DECREF( tmp_left_name_1 );
    Py_DECREF( tmp_right_name_2 );
    if ( tmp_tuple_element_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_args_name_1 );

        frame_module->f_lineno = 32;
        goto frame_exception_exit_1;
    }
    PyTuple_SET_ITEM( tmp_args_name_1, 0, tmp_tuple_element_1 );
    tmp_kw_name_2 = PyDict_Copy( const_dict_a0adbc06b00682b62dab9d9190a1ebe9 );
    frame_module->f_lineno = 32;
    tmp_unused = CALL_FUNCTION( tmp_called_name_5, tmp_args_name_1, tmp_kw_name_2 );
    Py_DECREF( tmp_args_name_1 );
    Py_DECREF( tmp_kw_name_2 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 32;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    loop_start_1:;
    tmp_len_arg_1 = GET_STRING_DICT_VALUE( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_desu );

    if (unlikely( tmp_len_arg_1 == NULL ))
    {
        tmp_len_arg_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_desu );
    }

    if ( tmp_len_arg_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 76 ], 26, 0 );
        exception_tb = NULL;

        frame_module->f_lineno = 33;
        goto frame_exception_exit_1;
    }

    tmp_compare_left_1 = BUILTIN_LEN( tmp_len_arg_1 );
    if ( tmp_compare_left_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 33;
        goto frame_exception_exit_1;
    }
    tmp_compare_right_1 = const_int_pos_290;
    tmp_cmp_Lt_1 = RICH_COMPARE_BOOL_LT( tmp_compare_left_1, tmp_compare_right_1 );
    if ( tmp_cmp_Lt_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_compare_left_1 );

        frame_module->f_lineno = 33;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_compare_left_1 );
    if (tmp_cmp_Lt_1 == 1)
    {
        goto branch_no_1;
    }
    else
    {
        goto branch_yes_1;
    }
    branch_yes_1:;
    goto loop_end_1;
    branch_no_1:;
    tmp_left_name_3 = GET_STRING_DICT_VALUE( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_wait );

    if (unlikely( tmp_left_name_3 == NULL ))
    {
        tmp_left_name_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_wait );
    }

    if ( tmp_left_name_3 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 102 ], 26, 0 );
        exception_tb = NULL;

        frame_module->f_lineno = 34;
        goto frame_exception_exit_1;
    }

    tmp_right_name_3 = const_int_pos_1;
    tmp_assign_source_9 = BINARY_OPERATION( PyNumber_InPlaceAdd, tmp_left_name_3, tmp_right_name_3 );
    if ( tmp_assign_source_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 34;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_wait, tmp_assign_source_9 );
    tmp_compare_left_2 = GET_STRING_DICT_VALUE( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_wait );

    if (unlikely( tmp_compare_left_2 == NULL ))
    {
        tmp_compare_left_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_wait );
    }

    if ( tmp_compare_left_2 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 102 ], 26, 0 );
        exception_tb = NULL;

        frame_module->f_lineno = 35;
        goto frame_exception_exit_1;
    }

    tmp_compare_right_2 = const_int_pos_6000;
    tmp_cmp_GtE_1 = RICH_COMPARE_BOOL_GE( tmp_compare_left_2, tmp_compare_right_2 );
    if ( tmp_cmp_GtE_1 == -1 )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 35;
        goto frame_exception_exit_1;
    }
    if (tmp_cmp_GtE_1 == 1)
    {
        goto branch_yes_2;
    }
    else
    {
        goto branch_no_2;
    }
    branch_yes_2:;
    tmp_source_name_6 = GET_STRING_DICT_VALUE( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_desu );

    if (unlikely( tmp_source_name_6 == NULL ))
    {
        tmp_source_name_6 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_desu );
    }

    if ( tmp_source_name_6 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 76 ], 26, 0 );
        exception_tb = NULL;

        frame_module->f_lineno = 36;
        goto frame_exception_exit_1;
    }

    tmp_called_name_6 = LOOKUP_ATTRIBUTE( tmp_source_name_6, const_str_plain_extend );
    if ( tmp_called_name_6 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 36;
        goto frame_exception_exit_1;
    }
    tmp_call_arg_element_3 = const_str_digest_137c0bc657f171dfd78596f46e2c2392;
    frame_module->f_lineno = 36;
    tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_6, tmp_call_arg_element_3 );
    Py_DECREF( tmp_called_name_6 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 36;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_assign_source_10 = const_int_0;
    UPDATE_STRING_DICT0( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_wait, tmp_assign_source_10 );
    branch_no_2:;
    tmp_called_name_7 = LOOKUP_BUILTIN( const_str_plain_print );
    if ( tmp_called_name_7 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 38;
        goto frame_exception_exit_1;
    }
    tmp_args_name_2 = PyTuple_New( 1 );
    tmp_subscribed_name_3 = GET_STRING_DICT_VALUE( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_color );

    if (unlikely( tmp_subscribed_name_3 == NULL ))
    {
        tmp_subscribed_name_3 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_color );
    }

    if ( tmp_subscribed_name_3 == NULL )
    {
        Py_DECREF( tmp_args_name_2 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 49 ], 27, 0 );
        exception_tb = NULL;

        frame_module->f_lineno = 38;
        goto frame_exception_exit_1;
    }

    tmp_subscript_name_3 = const_str_plain_cyan;
    tmp_left_name_4 = LOOKUP_SUBSCRIPT( tmp_subscribed_name_3, tmp_subscript_name_3 );
    if ( tmp_left_name_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_args_name_2 );

        frame_module->f_lineno = 38;
        goto frame_exception_exit_1;
    }
    tmp_source_name_7 = const_str_empty;
    tmp_called_name_8 = LOOKUP_ATTRIBUTE( tmp_source_name_7, const_str_plain_join );
    if ( tmp_called_name_8 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_args_name_2 );
        Py_DECREF( tmp_left_name_4 );

        frame_module->f_lineno = 38;
        goto frame_exception_exit_1;
    }
    tmp_args_element_name_2 = GET_STRING_DICT_VALUE( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_desu );

    if (unlikely( tmp_args_element_name_2 == NULL ))
    {
        tmp_args_element_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_desu );
    }

    if ( tmp_args_element_name_2 == NULL )
    {
        Py_DECREF( tmp_args_name_2 );
        Py_DECREF( tmp_left_name_4 );
        Py_DECREF( tmp_called_name_8 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 76 ], 26, 0 );
        exception_tb = NULL;

        frame_module->f_lineno = 38;
        goto frame_exception_exit_1;
    }

    frame_module->f_lineno = 38;
    tmp_right_name_4 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_8, tmp_args_element_name_2 );
    Py_DECREF( tmp_called_name_8 );
    if ( tmp_right_name_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_args_name_2 );
        Py_DECREF( tmp_left_name_4 );

        frame_module->f_lineno = 38;
        goto frame_exception_exit_1;
    }
    tmp_tuple_element_2 = BINARY_OPERATION_ADD( tmp_left_name_4, tmp_right_name_4 );
    Py_DECREF( tmp_left_name_4 );
    Py_DECREF( tmp_right_name_4 );
    if ( tmp_tuple_element_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_args_name_2 );

        frame_module->f_lineno = 38;
        goto frame_exception_exit_1;
    }
    PyTuple_SET_ITEM( tmp_args_name_2, 0, tmp_tuple_element_2 );
    tmp_kw_name_3 = _PyDict_NewPresized( 1 );
    tmp_left_name_5 = const_str_chr_13;
    tmp_subscribed_name_4 = GET_STRING_DICT_VALUE( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_color );

    if (unlikely( tmp_subscribed_name_4 == NULL ))
    {
        tmp_subscribed_name_4 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_color );
    }

    if ( tmp_subscribed_name_4 == NULL )
    {
        Py_DECREF( tmp_args_name_2 );
        Py_DECREF( tmp_kw_name_3 );
        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = UNSTREAM_STRING( &constant_bin[ 49 ], 27, 0 );
        exception_tb = NULL;

        frame_module->f_lineno = 38;
        goto frame_exception_exit_1;
    }

    tmp_subscript_name_4 = const_str_plain_off;
    tmp_right_name_5 = LOOKUP_SUBSCRIPT( tmp_subscribed_name_4, tmp_subscript_name_4 );
    if ( tmp_right_name_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_args_name_2 );
        Py_DECREF( tmp_kw_name_3 );

        frame_module->f_lineno = 38;
        goto frame_exception_exit_1;
    }
    tmp_dict_value_1 = BINARY_OPERATION_ADD( tmp_left_name_5, tmp_right_name_5 );
    Py_DECREF( tmp_right_name_5 );
    if ( tmp_dict_value_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );
        Py_DECREF( tmp_args_name_2 );
        Py_DECREF( tmp_kw_name_3 );

        frame_module->f_lineno = 38;
        goto frame_exception_exit_1;
    }
    tmp_dict_key_1 = const_str_plain_end;
    PyDict_SetItem( tmp_kw_name_3, tmp_dict_key_1, tmp_dict_value_1 );
    Py_DECREF( tmp_dict_value_1 );
    frame_module->f_lineno = 38;
    tmp_unused = CALL_FUNCTION( tmp_called_name_7, tmp_args_name_2, tmp_kw_name_3 );
    Py_DECREF( tmp_args_name_2 );
    Py_DECREF( tmp_kw_name_3 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 38;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    if ( CONSIDER_THREADING() == false )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 33;
        goto frame_exception_exit_1;
    }
    goto loop_start_1;
    loop_end_1:;
    tmp_called_name_9 = LOOKUP_BUILTIN( const_str_plain_print );
    if ( tmp_called_name_9 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 39;
        goto frame_exception_exit_1;
    }
    tmp_call_arg_element_4 = const_str_newline;
    frame_module->f_lineno = 39;
    tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_9, tmp_call_arg_element_4 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 39;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_import_globals_3 = ((PyModuleObject *)module_Loadingbar)->md_dict;
    frame_module->f_lineno = 40;
    tmp_assign_source_11 = IMPORT_MODULE( const_str_plain_kazooquest, tmp_import_globals_3, tmp_import_globals_3, Py_None, const_int_neg_1 );
    if ( tmp_assign_source_11 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        frame_module->f_lineno = 40;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_Loadingbar, (Nuitka_StringObject *)const_str_plain_kazooquest, tmp_assign_source_11 );

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION( frame_module );
#endif
    popFrameStack();

    assertFrameObject( frame_module );
    Py_DECREF( frame_module );

    goto frame_no_exception_1;
    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_module );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( frame_module );
    }
    else if ( exception_tb->tb_frame != frame_module )
    {
        PyTracebackObject *traceback_new = MAKE_TRACEBACK( frame_module );
        traceback_new->tb_next = exception_tb;
        exception_tb = traceback_new;
    }

    // Put the previous frame back on top.
    popFrameStack();

#if PYTHON_VERSION >= 340
    frame_module->f_executing -= 1;
#endif
    Py_DECREF( frame_module );

    // Return the error.
    goto module_exception_exit;
    frame_no_exception_1:;

    return MOD_RETURN_VALUE( module_Loadingbar );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
