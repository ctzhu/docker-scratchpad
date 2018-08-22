# FROM debian:stretch
FROM ubuntu:xenial
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

ADD https://raw.githubusercontent.com/ctzhu/docker-scratchpad/master/firefox-conda35/bashrc /root/.bashrc
ADD https://raw.githubusercontent.com/ctzhu/nvimfiles/master/init.vim /root/.config/nvim/init.vim
ADD https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim /root/.config/nvim/autoload/plug.vim
ADD https://tpo.pe/pathogen.vim /root/.config/nvim/autoload/pathogen.vim
ADD http://download.eclipse.org/jdtls/snapshots/jdt-language-server-0.24.0-201808202217.tar.gz /root/src/jdtls/jdtls.tar.gz

RUN apt-get update && apt-get install -y curl tmux screen unzip libgconf-2-4 \
    wget bzip2 ca-certificates curl grep sed dpkg \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion python-pip software-properties-common

RUN apt-add-repository ppa:neovim-ppa/unstable && apt-get update && apt-get install neovim -y

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.2.12-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

RUN apt-get update --fix-missing && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

RUN /opt/conda/bin/conda config --append channels r && \
    /opt/conda/bin/conda update conda -y && \
    /opt/conda/bin/conda install mro-base r-callr r-jsonlite r-lintr r-R6 r-repr r-stringr r-crayon r-rlang r-assertthat r-pillar r-processx r-backports r-cli r-purrr r-rprojroot r-tibble r-withr ipython pandas numpy scipy jupyter matplotlib openjdk maven nodejs mkl -y && \
    /usr/bin/pip install neovim && \
    /opt/conda/bin/pip install neovim awscli python-language-server python-language-server[all] && \
    /opt/conda/bin/conda clean -all -y && \
    /opt/conda/bin/Rscript -e "install.packages('languageserver', repo='https://cran.r-project.org')" && \
    cd /root/src/jdtls && tar xvzf /root/src/jdtls/jdtls.tar.gz && rm /root/src/jdtls/jdtls.tar.gz

RUN echo "#!/bin/bash" >> /usr/bin/jdtls && \
    echo "server=/root/src/jdtls" >> /usr/bin/jdtls && \
    echo "version=1.5.100.v20180611-1436" >> /usr/bin/jdtls && \
    echo "java \\" >> /usr/bin/jdtls && \
    echo "    -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=1044 \\" >> /usr/bin/jdtls && \
    echo "    -Declipse.application=org.eclipse.jdt.ls.core.id1 \\" >> /usr/bin/jdtls && \
    echo "    -Dosgi.bundles.defaultStartLevel=4 \\" >> /usr/bin/jdtls && \
    echo "    -Declipse.product=org.eclipse.jdt.ls.core.product \\" >> /usr/bin/jdtls && \
    echo "    -Dlog.level=ALL \\" >> /usr/bin/jdtls && \
    echo "    -noverify \\" >> /usr/bin/jdtls && \
    echo "    -Xmx1G \\" >> /usr/bin/jdtls && \
    echo "    -jar \$server/plugins/org.eclipse.equinox.launcher_\$version.jar \\" >> /usr/bin/jdtls && \
    echo "    -configuration \$server/config_linux -data ~ \$@" >> /usr/bin/jdtls && \
    chmod +x /usr/bin/jdtls && \
    chmod +x /usr/bin/nvim

ENV PATH /opt/conda/bin:$PATH
ENV LS_COLORS rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
CMD [ "/bin/bash" ]
