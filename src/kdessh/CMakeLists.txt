project(kdessh)

set(kdessh_SRCS kdessh.cpp sshdlg.cpp )

kde4_add_executable(kdessh ${kdessh_SRCS})

target_link_libraries(kdessh   ${KDE4_KDESU_LIBS} ${KDE4_KDE3SUPPORT_LIBS}  )

install(TARGETS kdessh  ${INSTALL_TARGETS_DEFAULT_ARGS} )
