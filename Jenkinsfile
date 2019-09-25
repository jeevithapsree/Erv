node {
    //Paramaters passing
    properties([disableConcurrentBuilds(), parameters([string(defaultValue: 'ecr', description: '', name: 'image_name', trim: true)])])
    
     stage ('checkout') {
      //  git credentialsId: '7c01b196-3329-4366-94a8-3627af872853', url: 'git@github.com:hari212008/Erv.git'
	git branch: 'develop', credentialsId: '7c01b196-3329-4366-94a8-3627af872853', url: 'https://github.com/hari212008/Erv.git'   
 }
    
    stage ('Copying EDA&Data processing scripts') {
        sh 'sudo cp -R erv/ /jenkins/terraform/modules/usecase-setup/source'               
    }
    
  
    stage ('Terraform-checkout') {
        //git credentialsId: '7c01b196-3329-4366-94a8-3627af872853', url: 'git@github.com:hari212008/terrafrm.git'
        git branch: 'develop', credentialsId: '7c01b196-3329-4366-94a8-3627af872853', poll: false, url: 'github.com:hari212008/terrafrm.git'
        }
     stage ('Notebook-Initialise'){
    dir ('erv/'){
        sh '''terraform --version
            pwd'''
        sh 'terraform init'
            }
        }
    stage ('Terraform-Plan'){
    dir ('erv/') {
      sh 'terraform get --update'
      sh 'terraform plan '
           
    }
    stage ('ERV-Apply'){
      dir('erv/') {
      sh 'terraform destroy -auto-approve'
      }
    }
    }
}
