project( kdeutils )

set( CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake/modules )

# search packages used by KDE
find_package( KDE4 REQUIRED )
find_package( LibKNotificationItem-1 REQUIRED )

include( KDE4Defaults )
include( MacroLibrary )

# If definitions like -D_GNU_SOURCE are needed for these checks they
# should be added to _KDE4_PLATFORM_DEFINITIONS when it is originally
# defined outside this file.  Here we include these definitions in
# CMAKE_REQUIRED_DEFINITIONS so they will be included in the build of
# checks below.
set( CMAKE_REQUIRED_DEFINITIONS ${_KDE4_PLATFORM_DEFINITIONS} )

add_definitions( ${QT_DEFINITIONS} ${KDE4_DEFINITIONS} )
include_directories( ${CMAKE_SOURCE_DIR} ${CMAKE_BINARY_DIR} ${KDE4_INCLUDES} ${LIBKNOTIFICATIONITEM-1_INCLUDE_DIR})

# --- check for dependencies ---
if(X11_FOUND)
  macro_optional_find_package( QImageBlitz )
  macro_log_feature( QIMAGEBLITZ_FOUND "QImageBlitz" "An image effects library" "kdesupport" FALSE "" "Required for building SuperKaramba.")
endif(X11_FOUND)
macro_optional_find_package( GMP )
macro_log_feature( GMP_FOUND "GMP" "The GNU Multiple Precision Arithmetic Library" "http://www.swox.com/gmp" FALSE "" "Required for building KCalc.")
macro_optional_find_package( QCA2 )
macro_log_feature( QCA2_FOUND "QCA2" "Qt Cryptographic Architecture" "http://delta.affinix.com/qca" FALSE "2.0.0" "Needed for most of the algorithms of the checksum tool in Okteta." )

# --- docs ---
macro_optional_add_subdirectory( doc )

# --- programs ---
# listed alphabetically, each with own guards
macro_optional_add_subdirectory( ark )
if( GMP_FOUND )
    macro_optional_add_subdirectory( kcalc )
endif( GMP_FOUND )
if( UNIX )
    macro_optional_add_subdirectory( kdessh )
    macro_optional_add_subdirectory( kdelirc )
    macro_optional_add_subdirectory( kdf )
    # K3Process
    macro_optional_add_subdirectory( kfloppy )
    macro_optional_add_subdirectory( printer-applet )
endif( UNIX )

macro_optional_add_subdirectory( kcharselect )
macro_optional_add_subdirectory( kgpg )
macro_optional_add_subdirectory( ktimer )
macro_optional_add_subdirectory( kwallet )
macro_optional_add_subdirectory( okteta )
macro_optional_add_subdirectory( sweeper )

if( X11_FOUND AND QIMAGEBLITZ_FOUND)
    #find_file( BACKGROUND_INTERFACE_FILE_FOUND org.kde.kdesktop.Background.xml PATHS ${DBUS_INTERFACES_INSTALL_DIR} )

    #if( BACKGROUND_INTERFACE_FILE_FOUND )
        macro_optional_add_subdirectory( superkaramba )
    #else( BACKGROUND_INTERFACE_FILE_FOUND )
        #MESSAGE( STATUS "org.kde.kdesktop.Background.xml was not found install kdebase before please" )
    #endif( BACKGROUND_INTERFACE_FILE_FOUND )
endif( X11_FOUND AND QIMAGEBLITZ_FOUND)

# --- show log ---
macro_display_feature_log()
