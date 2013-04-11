# Transdroider

A couple of **Python** scripts: one for create an **MS Excel** book from every strings.xml file in your Android project. Other to create all the res/values-xx structure and strings.xml files from an MS Excel book. For those not using **xliff** or **gettext**...

## XML from Excel (i18n_xml_from_excel.py)

Create full directory structure (also lang code suffix) and localised string.xml files for an Android project from an MS Excel file.

Excel file must contain only one sheet (it can contain several sheets, but only the first one will be read) with strings following the next structure:

```text
------------------------------------------------
|         |  lang_code_1  |  lang_code_2  |  ...
------------------------------------------------
|  key_1  |  translation  |  translation  |  ...
------------------------------------------------
|  key_2  |  translation  |  translation  |  ...
     .            .               .
     .            .               .
     .            .               .
```

An example Excel file could look like:

```text
---------------------------------------------------------
|               |       en       |      es-rES     |  ...
---------------------------------------------------------
|  hello_world  |  Hello world!  |  ¡Hola, mundo!  |  ...
---------------------------------------------------------
|   good_bye    |    Good bye    |      Adiós      |  ...
        .                .                .
        .                .                .
        .                .                .
```

### Usage


`python i18n_xml_from_excel.py -f <input_excel_file> [-c]`

- option **-c**. If used, strings will be 'cleaned' before writing them to the XML file. See function `getCleanString` in code for further info.

## Excel from XML

Builds an MS Excel sheet with all the strings defined in every strings.xml file from an Android project separated in columns.

Excel output file will follow the next structure:

```text
------------------------------------------------
|  keys   |  lang_code_1  |  lang_code_2  |  ...
------------------------------------------------
|  key_1  |  translation  |  translation  |  ...
------------------------------------------------
|  key_2  |  translation  |  translation  |  ...
     .            .               .
     .            .               .
     .            .               .
```

An example sheet could look like:

```text
---------------------------------------------------------
|               |       en       |      es-rES     |  ...
---------------------------------------------------------
|  hello_world  |  Hello world!  |  ¡Hola, mundo!  |  ...
---------------------------------------------------------
|   good_bye    |    Good bye    |      Adiós      |  ...
        .                .                .
        .                .                .
        .                .                .
```

### Usage

`i18n_excel_from_android.py -d <android_project_root_directory> -o <output_excel_file_name>`

## Dependencies

* Python 2.7.2 (older versions not tested)
* `xlwt` and `xlrd` from Excel library, found at http://www.python-excel.org/
* Modules used: `optparse`, `codecs`, `os`, `glob xml.dom.minidom`

## Developed by

Miguel Barrios - mbarrben@gmail.com

## License

```text
Copyright 2013 Miguel Barrios

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
