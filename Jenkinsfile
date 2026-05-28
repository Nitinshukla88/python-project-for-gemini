pipeline {
    agent any 
    stages {
        stage("build") {
            steps {
               /* Here only Linux commands are allowed to write 
               for example echo "hello world " or for node or js environment, you can write sh 'npm run install' or 'npm run build'
              */ 
              echo 'building the application'
            }
        }
        stage("test") {
            steps {
                echo 'testing the application'
            }
        }
        stage("deploy") {
            steps {
                echo 'deploying the application'
            }
        }
    }
}
