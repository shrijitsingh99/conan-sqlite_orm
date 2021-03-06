from conans import ConanFile, tools
import os


class sqlite_ormConan(ConanFile):
    name = "sqlite_orm"
    version = "1.4"
    description = "SQLite ORM light header only library for modern C++."
    url = "https://github.com/bincrafters/conan-sqlite_orm"
    homepage = "https://github.com/fnc12/sqlite_orm"
    topics = ("conan", "sqlite", "sql", "database", "orm", "sqlite_orm")
    author = "AlexandrePTJ <alpetitjean@gmail.com>"
    license = "BSD 3-Clause"
    requires = "sqlite3/3.21.0@bincrafters/stable"
    _source_subfolder = "source_subfolder"
    no_copy_source = True

    def source(self):
        source_url = "https://github.com/fnc12/sqlite_orm"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
