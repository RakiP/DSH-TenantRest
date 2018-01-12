node {
    def app
stage('clone repo') {
       git 'GITURL'
       //git 'https://git.kpn.org/projects/TQR/repos/dsh-testcases/browse'
            sh 'echo "clone successfull"'
    }
    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */
        // git 'https://github.com/RakiP/dockerRF'
         sh 'rsync -avz -e "sshpass -p PASSWORD ssh -o StrictHostKeyChecking=no" . USERNAME@IPADDRESS:PATHTOMOUNTEDDISK'
        sh 'echo "push to mounted disk successfull"'
    }
    }