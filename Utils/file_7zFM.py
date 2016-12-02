
files_c=[
 'C/7zCrc.c',
 'C/7zCrcOpt.c',
 'C/Alloc.c',
 'C/CpuArch.c',
 'C/Sha256.c',
 'C/Sort.c',
 'C/Threads.c',
]

files_cpp=[
 'CPP/7zip/Archive/Common/OutStreamWithCRC.cpp',
 'CPP/7zip/Common/CreateCoder.cpp',
 'CPP/7zip/Common/FilePathAutoRename.cpp',
 'CPP/7zip/Common/FileStreams.cpp',
 'CPP/7zip/Common/FilterCoder.cpp',
 'CPP/7zip/Common/LimitedStreams.cpp',
 'CPP/7zip/Common/MethodProps.cpp',
 'CPP/7zip/Common/ProgressUtils.cpp',
 'CPP/7zip/Common/PropId.cpp',
 'CPP/7zip/Common/StreamObjects.cpp',
 'CPP/7zip/Common/StreamUtils.cpp',
 'CPP/7zip/Common/UniqBlocks.cpp',
 'CPP/7zip/Compress/CopyCoder.cpp',
 'CPP/7zip/UI/Agent/Agent.cpp',
 'CPP/7zip/UI/Agent/AgentOut.cpp',
 'CPP/7zip/UI/Agent/AgentProxy.cpp',
 'CPP/7zip/UI/Agent/ArchiveFolder.cpp',
 'CPP/7zip/UI/Agent/ArchiveFolderOpen.cpp',
 'CPP/7zip/UI/Agent/ArchiveFolderOut.cpp',
 'CPP/7zip/UI/Agent/UpdateCallbackAgent.cpp',
 'CPP/7zip/UI/Common/ArchiveExtractCallback.cpp',
 'CPP/7zip/UI/Common/ArchiveName.cpp',
 'CPP/7zip/UI/Common/ArchiveOpenCallback.cpp',
 'CPP/7zip/UI/Common/CompressCall.cpp',
 'CPP/7zip/UI/Common/DefaultName.cpp',
 'CPP/7zip/UI/Common/EnumDirItems.cpp',
 'CPP/7zip/UI/Common/ExtractingFilePath.cpp',
 'CPP/7zip/UI/Common/HashCalc.cpp',
 'CPP/7zip/UI/Common/LoadCodecs.cpp',
 'CPP/7zip/UI/Common/OpenArchive.cpp',
 'CPP/7zip/UI/Common/PropIDUtils.cpp',
 'CPP/7zip/UI/Common/SetProperties.cpp',
 'CPP/7zip/UI/Common/SortUtils.cpp',
 'CPP/7zip/UI/Common/UpdateAction.cpp',
 'CPP/7zip/UI/Common/UpdateCallback.cpp',
 'CPP/7zip/UI/Common/UpdatePair.cpp',
 'CPP/7zip/UI/Common/UpdateProduce.cpp',
 'CPP/7zip/UI/Common/WorkDir.cpp',
 'CPP/7zip/UI/Common/ZipRegistry.cpp',
 'CPP/7zip/UI/FileManager/App.cpp',
 'CPP/7zip/UI/FileManager/ClassDefs.cpp',
 'CPP/7zip/UI/FileManager/ComboDialog.cpp',
 'CPP/7zip/UI/FileManager/ComboDialog_rc.cpp',
 'CPP/7zip/UI/FileManager/CopyDialog.cpp',
 'CPP/7zip/UI/FileManager/CopyDialog_rc.cpp',
 'CPP/7zip/UI/FileManager/ExtractCallback.cpp',
 'CPP/7zip/UI/FileManager/FM.cpp',
 'CPP/7zip/UI/FileManager/FM_rc.cpp',
 'CPP/7zip/UI/FileManager/FSDrives.cpp',
 'CPP/7zip/UI/FileManager/FSFolder.cpp',
 'CPP/7zip/UI/FileManager/FSFolderCopy.cpp',
 'CPP/7zip/UI/FileManager/FileFolderPluginOpen.cpp',
 'CPP/7zip/UI/FileManager/FormatUtils.cpp',
 'CPP/7zip/UI/FileManager/LangUtils.cpp',
 'CPP/7zip/UI/FileManager/ListViewDialog.cpp',
 'CPP/7zip/UI/FileManager/ListViewDialog_rc.cpp',
 'CPP/7zip/UI/FileManager/MessagesDialog.cpp',
 'CPP/7zip/UI/FileManager/MessagesDialog_rc.cpp',
 'CPP/7zip/UI/FileManager/MyLoadMenu.cpp',
 'CPP/7zip/UI/FileManager/OpenCallback.cpp',
 'CPP/7zip/UI/FileManager/OverwriteDialog.cpp',
 'CPP/7zip/UI/FileManager/OverwriteDialog_rc.cpp',
 'CPP/7zip/UI/FileManager/Panel.cpp',
 'CPP/7zip/UI/FileManager/PanelCopy.cpp',
 'CPP/7zip/UI/FileManager/PanelCrc.cpp',
 'CPP/7zip/UI/FileManager/PanelFolderChange.cpp',
 'CPP/7zip/UI/FileManager/PanelItemOpen.cpp',
 'CPP/7zip/UI/FileManager/PanelItems.cpp',
 'CPP/7zip/UI/FileManager/PanelListNotify.cpp',
 'CPP/7zip/UI/FileManager/PanelMenu.cpp',
 'CPP/7zip/UI/FileManager/PanelOperations.cpp',
 'CPP/7zip/UI/FileManager/PanelSelect.cpp',
 'CPP/7zip/UI/FileManager/PanelSort.cpp',
 'CPP/7zip/UI/FileManager/PanelSplitFile.cpp',
 'CPP/7zip/UI/FileManager/PasswordDialog.cpp',
 'CPP/7zip/UI/FileManager/PasswordDialog_rc.cpp',
 'CPP/7zip/UI/FileManager/ProgramLocation.cpp',
 'CPP/7zip/UI/FileManager/ProgressDialog2.cpp',
 'CPP/7zip/UI/FileManager/ProgressDialog2_rc.cpp',
 'CPP/7zip/UI/FileManager/PropertyName.cpp',
 'CPP/7zip/UI/FileManager/RegistryUtils.cpp',
 'CPP/7zip/UI/FileManager/RootFolder.cpp',
 'CPP/7zip/UI/FileManager/SplitDialog.cpp',
 'CPP/7zip/UI/FileManager/SplitDialog_rc.cpp',
 'CPP/7zip/UI/FileManager/SplitUtils.cpp',
 'CPP/7zip/UI/FileManager/StringUtils.cpp',
 'CPP/7zip/UI/FileManager/SysIconUtils.cpp',
 'CPP/7zip/UI/FileManager/TextPairs.cpp',
 'CPP/7zip/UI/FileManager/UpdateCallback100.cpp',
 'CPP/7zip/UI/FileManager/ViewSettings.cpp',
 'CPP/7zip/UI/FileManager/wxFM.cpp',
 'CPP/7zip/UI/GUI/HashGUI.cpp',
 'CPP/7zip/UI/GUI/UpdateCallbackGUI2.cpp',
 'CPP/Common/CRC.cpp',
 'CPP/Common/CrcReg.cpp',
 'CPP/Common/IntToString.cpp',
 'CPP/Common/Lang.cpp',
 'CPP/Common/MyString.cpp',
 'CPP/Common/MyVector.cpp',
 'CPP/Common/MyWindows.cpp',
 'CPP/Common/NewHandler.cpp',
 'CPP/Common/StringConvert.cpp',
 'CPP/Common/StringToInt.cpp',
 'CPP/Common/TextConfig.cpp',
 'CPP/Common/UTFConvert.cpp',
 'CPP/Common/Wildcard.cpp',
 'CPP/Windows/Clipboard.cpp',
 'CPP/Windows/Control/Controls.cpp',
 'CPP/Windows/Control/Dialog.cpp',
 'CPP/Windows/Control/Window2.cpp',
 'CPP/Windows/DLL.cpp',
 'CPP/Windows/ErrorMsg.cpp',
 'CPP/Windows/FileDir.cpp',
 'CPP/Windows/FileFind.cpp',
 'CPP/Windows/FileIO.cpp',
 'CPP/Windows/FileName.cpp',
 'CPP/Windows/PropVariant.cpp',
 'CPP/Windows/PropVariantConv.cpp',
 'CPP/Windows/Registry.cpp',
 'CPP/Windows/Synchronization.cpp',
 'CPP/Windows/System.cpp',
 'CPP/Windows/TimeUtils.cpp',
 'CPP/Windows/Window.cpp',
 'CPP/myWindows/wine_GetXXXDefaultLangID.cpp',
 'CPP/myWindows/wine_date_and_time.cpp',
]

