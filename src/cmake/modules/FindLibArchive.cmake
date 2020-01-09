# - Try to find libarchive
# Once done this will define
#
#  LIBARCHIVE_FOUND - system has libarchive
#  LIBARCHIVE_INCLUDE_DIR - the libarchive include directory
#  LIBARCHIVE_LIBRARY - Link this to use libarchive
#
# Copyright (c) 2006, Pino Toscano, <toscano.pino@tiscali.it>
#
# Redistribution and use is allowed according to the terms of the BSD license.
# For details see the accompanying COPYING-CMAKE-SCRIPTS file.

include(CheckLibraryExists)

if (LIBARCHIVE_LIBRARY AND LIBARCHIVE_INCLUDE_DIR)
  # in cache already
  set(LIBARCHIVE_FOUND TRUE)
else (LIBARCHIVE_LIBRARY AND LIBARCHIVE_INCLUDE_DIR)

  find_path(LIBARCHIVE_INCLUDE_DIR archive.h
    ${GNUWIN32_DIR}/include
  )

  find_library(LIBARCHIVE_LIBRARY NAMES archive libarchive archive2 libarchive2
    PATHS
    ${GNUWIN32_DIR}/lib
  )

  if (LIBARCHIVE_LIBRARY)
    CHECK_LIBRARY_EXISTS(${LIBARCHIVE_LIBRARY} archive_write_set_compression_gzip PATHS HAVE_LIBARCHIVE_GZIP_SUPPORT)
  endif (LIBARCHIVE_LIBRARY)

  include(FindPackageHandleStandardArgs)
  FIND_PACKAGE_HANDLE_STANDARD_ARGS(LibArchive DEFAULT_MSG LIBARCHIVE_INCLUDE_DIR LIBARCHIVE_LIBRARY HAVE_LIBARCHIVE_GZIP_SUPPORT)

    # ensure that they are cached
    set(LIBARCHIVE_INCLUDE_DIR ${LIBARCHIVE_INCLUDE_DIR} CACHE INTERNAL "The libarchive include path")
    set(LIBARCHIVE_LIBRARY ${LIBARCHIVE_LIBRARY} CACHE INTERNAL "The libraries needed to use libarchive")

endif (LIBARCHIVE_LIBRARY AND LIBARCHIVE_INCLUDE_DIR)
