# -*- coding : utf-8 -*-

import hashlib

"""
=================================================================
===================ENGLISH-DOC===================================
=================================================================
=This is a module which has functions for calculating hash sums.=
=          For strings yet only works in Linux and Mac          =
=          Hash Name - hash Function()                          =
=          1.Md5 hash - hasMd5()                                =
=          2.sha1 hash - hasSha1()                              =
=          3.sha256 hash -  hasSha256()                         =
=          4.sha512 hash -  hasSha512()                         =
=          5.sha384 hash - hasSha384()                          =
=          6.sha224 hash - hasSha224()                          =
=          7.Md5 hash of string - hasMd5Str()                   =
=          8.sha1 hash of string - hasSha1Str()                 =
=          9.sha256 hash of string - hasSha256Str()             =
=          10.sha512 hash of string - hasSha512Str()            =
=          11.sha384 hash of string - hasSha384Str()            =
=          12.sha224 hash of string - hasSha224Str()            =
=================================================================
===================RUSSIAN-DOC===================================
=================================================================
=    Это модуль который имеет функции для расчета хеш сумм.     =
=          Для строк пока работает только в Linux and Mac       =
=          Вид хеш суммы - имя функции()                        =
=          1.Md5 хэш - hasMd5()                                 =
=          2.sha1 хеш - hasSha1()                               =
=          3.sha256 хеш - hasSha256()                           =
=          4.sha512 хеш - hasSha512()                           =
=          5.sha384 хеш - hasSha384()                           =
=          6.sha224 хеш - hasSha224()                           =
=          7.Md5 хэш строки - hasMd5Str()                       =
=          8.sha1 хеш строки - hasSha1Str()                     =
=          9.sha256 хеш строки - hasSha256Str()                 =
=          10.sha512 хеш строки - hasSha512Str()                =
=          11.sha384 хеш строки - hasSha384Str()                =
=          12.sha224 хеш строки - hasSha224Str()                =
=================================================================
=================================================================
=================================================================
"""

__author__ = 'yorick'


# =========================================================================================
# Функции расчета хеш сумм файлов
# =========================================================================================
# =========================================================================================
# Functions for calculating hash sums of files
# =========================================================================================
def hasMd5(filename):

    """
    ===================
    calculating md5 hash
    ===================
    расчитывает md5 хеш
    ===================
    """

    m = hashlib.md5()
    f = open(filename, 'rb')
    c = f.read()
    m.update(c)
    f.close()
    return m.hexdigest()


def hasSha256(filename):

    """
    =======================
    calculating sha256 hash
    =======================
    расчитывает sha256 хеш
    =======================
    """

    m = hashlib.sha256()
    f = open(filename, 'rb')
    c = f.read()
    m.update(c)
    f.close()
    return m.hexdigest()


def hasSha512(filename):

    """
    =======================
    calculating sha512 hash
    =======================
    расчитывает sha512 хеш
    =======================
    """

    m = hashlib.sha512()
    f = open(filename, 'rb')
    c = f.read()
    m.update(c)
    f.close()
    return m.hexdigest()


def hasSha384(filename):

    """
    =======================
    calculating sha384 hash
    =======================
    расчитывает sha384 хеш
    =======================
    """
    m = hashlib.sha384()
    f = open(filename, 'rb')
    c = f.read()
    m.update(c)
    f.close()
    return m.hexdigest()


def hasSha224(filename):

    """
    ========================
    calculating sha224 hash
    =======================
    расчитывает sha224 хеш
    =======================
    """

    m = hashlib.sha224()
    f = open(filename, 'rb')
    c = f.read()
    m.update(c)
    f.close()
    return m.hexdigest()


def hasSha1(filename):

    """
    =====================
    calculating sha1 hash
    =====================
    расчитывает sha1 хеш
    =====================
    """

    m = hashlib.sha1()
    f = open(filename, 'rb')
    c = f.read()
    m.update(c)
    f.close()
    return m.hexdigest()

# =========================================================================================
# Функции расчета хеш сумм для строк
# =========================================================================================
# =========================================================================================
#  Functions for calculating hash sums of strings
# =========================================================================================


def hasMd5Str(content):

    """
    ======================================
    calculating md5 hash of string content
    ======================================
    расчитывает md5 хеш строки content
    ======================================
    """

    content = content.encode('utf-8')
    m = hashlib.md5()
    m.update(content)
    return m.hexdigest()


def hasSha256Str(content):

    """
    =========================================
    calculating sha256 hash of string content
    =========================================
    расчитывает sha256 хеш строки content
    =========================================
    """

    content = content.encode('utf-8')
    m = hashlib.sha256()
    m.update(content)
    return m.hexdigest()


def hasSha512Str(content):

    """
    =========================================
    calculating sha512 hash of string content
    =========================================
    расчитывает sha512 хеш строки content
    =========================================
    """

    content = content.encode('utf-8')
    m = hashlib.sha512()
    m.update(content)
    return m.hexdigest()


def hasSha384Str(content):

    """
    =========================================
    calculating sha384 hash of string content
    =========================================
    расчитывает sha384 хеш строки content
    =========================================
    """

    content = content.encode('utf-8')
    m = hashlib.sha384()
    m.update(content)
    return m.hexdigest()


def hasSha224Str(content):

    """
    =========================================
    calculating sha224 hash of string content
    =========================================
    расчитывает sha224 хеш строки content
    =========================================
    """

    content = content.encode('utf-8')
    m = hashlib.sha224()
    m.update(content)
    return m.hexdigest()


def hasSha1Str(content):

    """
    =======================================
    calculating sha1 hash of string content
    =======================================
    расчитывает sha1 хеш строки content
    =======================================
    """

    content = content.encode('utf-8')
    m = hashlib.sha1()
    m.update(content)
    return m.hexdigest()
