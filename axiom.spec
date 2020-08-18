Name:                axiom
Version:             1.2.14
Release:             1
Epoch:               0
Summary:             Axis Object Model
License:             ASL 2.0
Url:                 http://ws.apache.org/commons/axiom/
Source0:             http://archive.apache.org/dist/ws/axiom/%{version}/axiom-%{version}-source-release.zip
Patch0:              port-to-mime4j-0.8.1.patch
BuildRequires:       maven-local mvn(commons-io:commons-io) mvn(commons-logging:commons-logging)
BuildRequires:       mvn(com.sun.xml.bind:jaxb-impl) mvn(javax.mail:mail)
BuildRequires:       mvn(javax.xml.bind:jaxb-api) mvn(jaxen:jaxen) mvn(junit:junit)
BuildRequires:       mvn(net.sf.saxon:saxon) mvn(org.apache:apache:pom:)
BuildRequires:       mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:       mvn(org.apache.james:apache-mime4j-core) >= 0.8.1
BuildRequires:       mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:       mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:       mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:       mvn(org.codehaus.woodstox:stax2-api)
BuildRequires:       mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires:       mvn(org.jvnet.jaxb2.maven2:maven-jaxb2-plugin) mvn(org.osgi:osgi.cmpn)
BuildRequires:       mvn(org.osgi:osgi.core) mvn(xalan:xalan) mvn(xerces:xercesImpl)
BuildRequires:       mvn(xmlunit:xmlunit)
Requires:            mvn(org.apache.james:apache-mime4j-core) >= 0.8.1
BuildArch:           noarch

%description
AXIOM stands for AXis Object Model (also known as OM - Object Model)
and refers to the XML info-set model that was initially developed for
Apache Axis2.

%package javadoc
Summary:             API Documentation for %{name}

%description javadoc
%{summary}.

%prep
%setup -q
%patch0
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :gmaven-plugin
%pom_remove_plugin :docbkx-maven-plugin
%pom_remove_plugin :build-helper-maven-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core
%pom_change_dep -r org.osgi:org.osgi.compendium org.osgi:osgi.cmpn
%pom_remove_dep :geronimo-activation_1.1_spec modules/axiom-{dom,parent,api,testutils,impl}
%pom_remove_dep :geronimo-stax-api_1.0_spec modules/axiom-{tests,parent,api,testutils,impl}
%pom_change_dep :geronimo-javamail_1.4_spec javax.mail:mail:1.4 modules/axiom-{dom,parent,api,impl}
%pom_remove_dep :saxon-dom modules/axiom-dom-testsuite
%pom_remove_plugin :maven-dependency-plugin modules/axiom-api
%pom_disable_module modules/axiom-osgi-tests
%pom_disable_module modules/axiom-integration
%pom_disable_module modules/axiom-samples
%mvn_package ":*-{tests,testsuite}" __noinstall
%mvn_package ":axiom-{build,test}utils" __noinstall

%build
%mvn_build -- -DskipTests

%install
%mvn_install

%files -f .mfiles
%doc *.txt
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Fri Aug 14 2020 leiju <leiju4@huawei.com> - 1.2.14-1
- Package init
