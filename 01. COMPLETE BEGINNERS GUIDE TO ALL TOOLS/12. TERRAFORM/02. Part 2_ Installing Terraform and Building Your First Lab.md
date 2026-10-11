# Part 2: Installing Terraform and Building Your First Lab

## Create Your Terraform Environment from Zero

Part 1 answered:

```text
What is Terraform?

Why does Infrastructure as Code exist?

What are providers?

What are resources?

Why does Terraform maintain state?

What does Write → Plan → Apply mean?
```

Now we stop talking only about Terraform.

We start using it.

By the end of this part, you will have:

```text
Terraform installed
Git installed
VS Code configured
Terraform editor support installed
AWS CLI introduced and optionally installed
A Terraform working directory
A real Terraform configuration
A provider downloaded
A dependency lock file
A Terraform-managed resource
Terraform state
A complete create/change/destroy lifecycle
A troubleshooting workflow
```

Most importantly, you will understand what Terraform creates on your computer and why.

---

# 1. What We Are Building

Our first architecture is intentionally simple:

```text
Local Machine
↓
Terraform CLI
↓
Local Provider
↓
First Managed Resource
```

The first managed resource will be a file on your computer.

The final result will look like:

```text
Terraform
↓
HashiCorp Local Provider
↓
veriqta-terraform.txt
```

This may look simple.

That is intentional.

The goal of the first lab is not to impress you with cloud architecture.

The goal is to understand Terraform itself.

---

# 2. Why We Are Not Creating AWS Infrastructure Yet

A beginner's first Terraform lab often tries to create an EC2 instance immediately.

That introduces several problems at once:

```text
Terraform installation
+
AWS account
+
AWS CLI
+
AWS credentials
+
IAM permissions
+
AWS networking
+
EC2
+
AMI selection
+
AWS Region
+
Cloud costs
+
Terraform
```

If something fails, the beginner may not know which layer caused the problem.

Instead, we will first learn:

```text
Terraform
Provider
Resource
State
Plan
Apply
Verification
Change
Destroy
```

using a local resource.

Then AWS can be introduced without Terraform itself being mysterious.

---

# 3. Our Complete Workflow

We will perform:

```text
Create Directory
↓
Write Configuration
↓
terraform init
↓
terraform fmt
↓
terraform validate
↓
terraform plan
↓
terraform apply
↓
Verify
↓
Modify
↓
Plan Again
↓
Apply Again
↓
Verify Again
↓
terraform destroy
↓
Verify Destruction
```

This is your first complete Terraform lifecycle.

---

# 4. What You Need

Required:

```text
Computer
Internet connection
Terminal
Terraform CLI
Text editor
```

Recommended:

```text
VS Code
HashiCorp Terraform VS Code extension
Git
AWS CLI v2
```

Supported learning environments include:

```text
Windows
macOS
Linux
```

You do not need an AWS account to complete the main lab in this part.

---

# 5. Before Installing Anything: Know Your Terminal

Terraform is primarily used through a command-line interface.

You therefore need a terminal.

## Windows

You can use:

```text
PowerShell
Windows Terminal
Command Prompt
```

For this series, PowerShell or Windows Terminal with PowerShell is recommended.

## macOS

Use:

```text
Terminal
```

or another terminal application.

## Linux

Use your distribution's terminal.

Common shells include:

```text
bash
zsh
```

---

# 6. What Is a CLI?

CLI means:

```text
Command-Line Interface
```

Instead of clicking buttons, you type commands.

Example:

```bash
terraform version
```

The shell finds the Terraform executable and runs it.

This introduces an important concept:

```text
PATH
```

---

# 7. What Is PATH?

Your operating system needs to know where executable programs are located.

When you type:

```bash
terraform
```

you are not usually typing the complete filesystem location of the Terraform executable.

Your shell searches directories listed in your:

```text
PATH
```

environment variable.

Conceptually:

```text
terraform
↓
Shell checks PATH
↓
Searches configured directories
↓
Finds Terraform executable
↓
Runs Terraform
```

---

# 8. Why PATH Matters

You may successfully download Terraform but still receive:

```text
terraform: command not found
```

or on Windows:

```text
'terraform' is not recognized...
```

That does not necessarily mean Terraform was not downloaded.

It may mean:

```text
Terraform executable exists
↓
but
↓
its directory is not in PATH
```

This distinction is important.

---

# 9. Check Whether Terraform Is Already Installed

Before installing anything, run:

```bash
terraform version
```

You may see output similar to:

```text
Terraform v1.x.x
on your-platform
```

The exact version and platform may differ.

If Terraform is already installed, do not blindly install another copy.

First determine which executable your shell is using.

Linux/macOS:

```bash
which terraform
```

Windows PowerShell:

```powershell
Get-Command terraform
```

This helps detect duplicate installations.

---

# 10. Terraform Installation Options

HashiCorp distributes Terraform as a standalone executable.

You can install it using:

```text
Package manager
```

or:

```text
Manual binary installation
```

Both approaches ultimately need this to work:

```text
Terminal
↓
terraform command
↓
Terraform executable
```

---

# 11. Current Terraform Version Note

At the time this guide was verified, HashiCorp's installation page lists:

```text
Terraform 1.16.3
```

Do not build your learning around memorizing that number.

Terraform changes over time.

Always verify the current supported release before installing or upgrading production environments.

In production, upgrading Terraform should be deliberate rather than automatic.

---

# 12. Installing Terraform on macOS with Homebrew

If Homebrew is already installed, HashiCorp provides an official tap.

Run:

```bash
brew tap hashicorp/tap
```

Then:

```bash
brew install hashicorp/tap/terraform
```

Verify:

```bash
terraform version
```

Expected structure:

```text
Terraform v1.x.x
on darwin_...
```

The architecture may show something such as:

```text
darwin_arm64
```

or:

```text
darwin_amd64
```

depending on the Mac.

---

# 13. Updating Terraform with Homebrew

If Terraform was installed using HashiCorp's Homebrew tap:

```bash
brew update
```

Then:

```bash
brew upgrade hashicorp/tap/terraform
```

Do not automatically upgrade production Terraform simply because a newer version exists.

Later we will learn version constraints and upgrade testing.

---

# 14. Installing Terraform on Windows

Terraform can be installed manually from HashiCorp's official release package.

HashiCorp's Terraform tutorial also documents Chocolatey installation:

```powershell
choco install terraform
```

Important:

Chocolatey is a third-party package manager.

HashiCorp does not maintain Chocolatey itself or its Terraform Chocolatey package.

For maximum control, especially in managed environments, use HashiCorp's official binary distribution.

---

# 15. Windows Manual Installation

The general process is:

```text
Download Terraform ZIP
↓
Extract terraform.exe
↓
Move terraform.exe to a dedicated directory
↓
Add that directory to PATH
↓
Open a new terminal
↓
terraform version
```

Example directory:

```text
C:\Tools\Terraform
```

Place:

```text
terraform.exe
```

inside it.

Then add:

```text
C:\Tools\Terraform
```

to your user or system PATH.

---

# 16. Editing PATH on Windows

Search Windows for:

```text
Edit environment variables for your account
```

Find:

```text
Path
```

Select:

```text
Edit
```

Add:

```text
C:\Tools\Terraform
```

Save the changes.

Close your existing terminal.

Open a new PowerShell window.

Run:

```powershell
terraform version
```

Why open a new terminal?

Because an already-running shell may still have the old environment.

---

# 17. Windows PATH Verification

Run:

```powershell
Get-Command terraform
```

You should see the path to the executable.

You can also inspect:

```powershell
$env:Path
```

If Terraform still cannot be found, investigate whether the directory containing `terraform.exe` is actually included.

---

# 18. Installing Terraform on Ubuntu/Debian

HashiCorp maintains an APT repository.

Install prerequisites if needed:

```bash
sudo apt-get update
sudo apt-get install -y wget gpg
```

Add HashiCorp's signing key:

```bash
wget -O - https://apt.releases.hashicorp.com/gpg \
  | sudo gpg --dearmor \
  -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
```

Add the HashiCorp repository:

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(grep -oP '(?<=UBUNTU_CODENAME=).*' /etc/os-release || lsb_release -cs) main" \
  | sudo tee /etc/apt/sources.list.d/hashicorp.list
```

Update package metadata:

```bash
sudo apt update
```

Install Terraform:

```bash
sudo apt install terraform
```

Verify:

```bash
terraform version
```

---

# 19. Installing Terraform on RHEL/CentOS

HashiCorp's current installation instructions use its RPM repository.

Install repository-management tooling:

```bash
sudo yum install -y yum-utils
```

Add the repository:

```bash
sudo yum-config-manager \
  --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
```

Install Terraform:

```bash
sudo yum -y install terraform
```

Verify:

```bash
terraform version
```

---

# 20. Installing Terraform on Fedora

Add HashiCorp's repository:

```bash
wget -O- https://rpm.releases.hashicorp.com/fedora/hashicorp.repo \
  | sudo tee /etc/yum.repos.d/hashicorp.repo
```

Install Terraform:

```bash
sudo dnf -y install terraform
```

Verify:

```bash
terraform version
```

---

# 21. Installing Terraform on Amazon Linux

HashiCorp's current installation instructions include:

```bash
sudo yum install -y yum-utils shadow-utils
```

Add the HashiCorp repository:

```bash
sudo yum-config-manager \
  --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
```

Install Terraform:

```bash
sudo yum install terraform
```

Verify:

```bash
terraform version
```

---

# 22. Manual Binary Installation

Package managers are convenient.

But understanding manual installation is useful because Terraform is fundamentally distributed as an executable binary.

The general process is:

```text
Identify OS
↓
Identify CPU architecture
↓
Download correct Terraform archive
↓
Verify download when required
↓
Extract archive
↓
Place executable in PATH
↓
Verify installation
```

---

# 23. CPU Architecture Matters

Common architecture names include:

```text
AMD64
ARM64
```

Examples:

Intel/AMD 64-bit PC:

```text
AMD64
```

Apple Silicon:

```text
ARM64
```

Many ARM-based Linux machines:

```text
ARM64
```

Downloading the wrong architecture can produce execution errors.

---

# 24. Check Architecture on Linux

Run:

```bash
uname -m
```

Possible results include:

```text
x86_64
```

or:

```text
aarch64
```

Common mapping:

```text
x86_64  → AMD64
aarch64 → ARM64
```

---

# 25. Check Architecture on macOS

Run:

```bash
uname -m
```

Possible results:

```text
arm64
```

or:

```text
x86_64
```

---

# 26. Manual Installation Principle

After extracting Terraform, the executable must live somewhere your shell can find it.

Common Unix-style locations include:

```text
/usr/local/bin
```

or a user-owned binary directory such as:

```text
$HOME/.local/bin
```

If you use a user-owned directory, ensure it is in PATH.

---

# 27. Check PATH on Linux/macOS

Run:

```bash
echo "$PATH"
```

You will see directories separated by colons.

Example:

```text
/usr/local/bin:/usr/bin:/bin
```

To find Terraform:

```bash
which terraform
```

---

# 28. Verify the Installation

Run:

```bash
terraform version
```

You can also use:

```bash
terraform -version
```

The important result is that Terraform executes successfully and identifies its version/platform.

Do not continue if:

```text
terraform command not found
```

Fix installation first.

---

# 29. Meet the Terraform CLI

Run:

```bash
terraform -help
```

or:

```bash
terraform --help
```

Terraform displays available commands and usage information.

You should see command categories including familiar commands such as:

```text
init
validate
plan
apply
destroy
fmt
output
show
state
version
```

The exact help output can change between Terraform releases.

---

# 30. Getting Help for a Specific Command

Instead of searching the internet every time, Terraform can show command-specific help.

Example:

```bash
terraform plan -help
```

Another example:

```bash
terraform init -help
```

Another:

```bash
terraform apply -help
```

Learn this habit.

CLI help is part of professional command-line work.

---

# 31. Terraform Command Structure

The general pattern is:

```text
terraform <command> [options]
```

Example:

```bash
terraform plan
```

Here:

```text
terraform
```

is the program.

```text
plan
```

is the command.

A command can have options.

Example:

```bash
terraform plan -no-color
```

Here:

```text
-no-color
```

is an option.

---

# 32. Do Not Memorize Flags Blindly

Use:

```bash
terraform <command> -help
```

before copying unfamiliar flags.

Example:

```bash
terraform init -help
```

This becomes increasingly important when we reach production automation.

---

# 33. Working Directories

Terraform normally operates on configuration in the current working directory.

Suppose you are inside:

```text
terraform-labs/
└── part-02-first-lab/
```

and that directory contains:

```text
main.tf
```

When you run:

```bash
terraform plan
```

Terraform evaluates the root module configuration in that working directory.

---

# 34. Check Your Current Directory

Linux/macOS:

```bash
pwd
```

PowerShell:

```powershell
Get-Location
```

This sounds trivial.

It is not.

Running Terraform from the wrong directory is a real operational mistake.

Always know:

```text
Where am I?

Which configuration am I operating?

Which state/backend belongs to this directory?
```

---

# 35. List Files Before Running Terraform

Linux/macOS:

```bash
ls -la
```

PowerShell:

```powershell
Get-ChildItem -Force
```

Before important Terraform operations, confirm you are in the intended directory.

---

# 36. Terraform Configuration Files

Terraform configuration files normally use:

```text
.tf
```

Example:

```text
main.tf
```

Other common names include:

```text
providers.tf
variables.tf
outputs.tf
versions.tf
network.tf
compute.tf
```

These names are organizational conventions.

Terraform does not execute them sequentially according to their filenames.

---

# 37. Terraform Reads the Module Configuration Together

Suppose a directory contains:

```text
main.tf
variables.tf
outputs.tf
```

Do not think:

```text
main.tf runs
↓
variables.tf runs
↓
outputs.tf runs
```

Instead:

```text
Terraform reads the configuration files
↓
Treats them as one module configuration
↓
Evaluates relationships
↓
Builds a dependency graph
```

This is important.

---

# 38. Creating the Lab Directory

Linux/macOS:

```bash
mkdir -p terraform-labs/part-02-first-lab
cd terraform-labs/part-02-first-lab
```

Verify:

```bash
pwd
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force terraform-labs\part-02-first-lab
Set-Location terraform-labs\part-02-first-lab
```

Verify:

```powershell
Get-Location
```

---

# 39. Our Initial Directory

At first:

```text
part-02-first-lab/
```

It is empty.

Verify.

Linux/macOS:

```bash
ls -la
```

PowerShell:

```powershell
Get-ChildItem -Force
```

---

# 40. Install Git

Git is not required for Terraform itself to execute this first lab.

But Infrastructure as Code belongs in version control.

Verify whether Git already exists:

```bash
git --version
```

Expected structure:

```text
git version x.x.x
```

---

# 41. Installing Git on Windows

Use the official Git for Windows distribution.

After installation, open a new terminal and run:

```powershell
git --version
```

---

# 42. Installing Git on macOS

If Homebrew is installed:

```bash
brew install git
```

Verify:

```bash
git --version
```

macOS may also provide Git through Apple's developer command-line tooling.

---

# 43. Installing Git on Ubuntu/Debian

Run:

```bash
sudo apt update
sudo apt install -y git
```

Verify:

```bash
git --version
```

---

# 44. Configure Git Identity

If Git has not been configured previously:

```bash
git config --global user.name "Your Name"
```

Then:

```bash
git config --global user.email "your-email@example.com"
```

Use your real development identity.

Verify:

```bash
git config --global --list
```

Do not copy the example email literally.

---

# 45. Initialize the Lab Repository

From:

```text
part-02-first-lab/
```

run:

```bash
git init
```

Expected structure now includes:

```text
part-02-first-lab/
└── .git/
```

`.git` is hidden on many systems.

---

# 46. Create `.gitignore`

Create:

```text
.gitignore
```

with:

```gitignore
.terraform/
*.tfstate
*.tfstate.*
crash.log
crash.*.log
*.tfplan
*.tfvars
*.tfvars.json
```

Important:

Do **not** add:

```text
.terraform.lock.hcl
```

to `.gitignore`.

We normally want the dependency lock file committed.

Also understand that ignoring all `.tfvars` is a conservative beginner policy. Teams sometimes deliberately commit non-sensitive variable files. Never commit secrets simply because a file is not ignored.

---

# 47. VS Code Setup

Install Visual Studio Code if you do not already have an editor.

Then open the project directory.

From a shell where the `code` command is configured:

```bash
code .
```

If `code` is unavailable, open VS Code normally and choose:

```text
File
↓
Open Folder
↓
part-02-first-lab
```

---

# 48. Terraform Support in VS Code

Install the official:

```text
HashiCorp Terraform
```

extension.

The extension provides Terraform editing capabilities through HashiCorp's Terraform language tooling.

Features include:

```text
syntax highlighting
IntelliSense
code navigation
formatting
language support
```

This improves editing.

It does not replace understanding Terraform.

---

# 49. Editor Support Is Not Terraform

Keep the layers separate.

```text
VS Code
=
Editor
```

```text
Terraform VS Code Extension
=
Editor assistance
```

```text
Terraform CLI
=
Terraform executable performing Terraform operations
```

You can use Terraform without VS Code.

You can also have the VS Code extension installed while Terraform itself is missing.

---

# 50. AWS CLI Introduction

This course eventually uses AWS heavily.

The AWS CLI is:

```text
AWS Command Line Interface
```

It allows you to interact with AWS services from a terminal.

Example:

```bash
aws sts get-caller-identity
```

That command can tell you which AWS identity the CLI is currently using.

We will not create AWS resources in the first lab.

---

# 51. Why Install AWS CLI Now?

Later our architecture becomes:

```text
Local Machine
├── Terraform CLI
└── AWS CLI
        ↓
AWS
```

Terraform and AWS CLI are different programs.

The AWS CLI is extremely useful for:

```text
authentication verification
resource inspection
troubleshooting
automation
cross-checking Terraform results
```

---

# 52. Verify AWS CLI

Run:

```bash
aws --version
```

If installed, you should see output beginning with something similar to:

```text
aws-cli/2...
```

For this series, AWS CLI version 2 is recommended.

---

# 53. AWS CLI Installation

AWS publishes current AWS CLI v2 installers for:

```text
Windows
macOS
Linux
```

Because AWS updates its installer instructions, use AWS's current official installation documentation rather than relying on old copied commands.

After installation, always verify:

```bash
aws --version
```

---

# 54. AWS Account Considerations

You do not need AWS for today's local Terraform lab.

Before future AWS labs, however, you will need an AWS account or authorized organizational AWS access.

Understand:

```text
AWS account
≠
AWS user
≠
IAM role
≠
AWS credentials
```

An AWS account is the security and billing boundary containing AWS resources.

An identity operates inside or through access to that account.

---

# 55. Do Not Use the AWS Root User for Everyday Terraform

The AWS account root user has extremely powerful access.

Do not use root credentials as your normal Terraform development identity.

Prefer appropriately controlled identities and permissions.

In organizational environments, authentication may be provided through:

```text
AWS IAM Identity Center
federation
IAM roles
workload identities
```

depending on the environment.

---

# 56. Credentials Basics

Terraform's AWS provider eventually needs a way to authenticate.

Conceptually:

```text
Terraform
↓
AWS Provider
↓
Credential Resolution
↓
AWS Identity
↓
AWS API
```

Credentials answer:

```text
Who is making this request?
```

IAM permissions answer:

```text
What is that identity allowed to do?
```

These are different questions.

---

# 57. Authentication vs Authorization

Authentication:

```text
Who are you?
```

Authorization:

```text
What can you do?
```

You can successfully authenticate to AWS and still receive:

```text
AccessDenied
```

because your identity lacks permission for a requested operation.

---

# 58. AWS IAM Identity Center

For workforce access, AWS supports IAM Identity Center authentication through the AWS CLI.

A configured profile can use:

```bash
aws configure sso
```

Then authenticate:

```bash
aws sso login --profile your-profile-name
```

And verify the caller:

```bash
aws sts get-caller-identity --profile your-profile-name
```

Your organization's setup determines the profile and permissions available to you.

Do not invent account IDs, roles, or SSO URLs.

---

# 59. Environment Variables

An environment variable is a named value available to a process through its environment.

Examples:

```text
PATH
AWS_REGION
AWS_PROFILE
```

AWS credential-related environment variables can also exist, including:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_SESSION_TOKEN
```

Temporary credentials commonly include a session token.

Do not hardcode real AWS credentials into Terraform `.tf` files.

---

# 60. Environment Variable Example on Linux/macOS

For a non-secret example:

```bash
export AWS_REGION=us-east-1
```

Verify:

```bash
echo "$AWS_REGION"
```

For a named AWS profile:

```bash
export AWS_PROFILE=your-profile-name
```

Verify:

```bash
echo "$AWS_PROFILE"
```

---

# 61. Environment Variable Example on PowerShell

Set a region for the current PowerShell session:

```powershell
$env:AWS_REGION = "us-east-1"
```

Verify:

```powershell
$env:AWS_REGION
```

Set a profile:

```powershell
$env:AWS_PROFILE = "your-profile-name"
```

---

# 62. Environment Variables Have Scope

A variable created in one terminal session may disappear when that terminal closes.

This is useful to understand.

A shell variable can be:

```text
temporary for one process/session
```

or configured persistently through operating-system/shell mechanisms.

Do not persist secrets carelessly.

---

# 63. Credential Precedence Matters

AWS tooling can obtain configuration and credentials from multiple sources.

For example:

```text
command-line settings
environment variables
profiles
role-based credentials
workload credentials
```

This creates a common troubleshooting problem:

```text
I expected Terraform to use identity A,
but it used identity B.
```

Always verify your active identity before important cloud operations.

Later we will use:

```bash
aws sts get-caller-identity
```

as a standard verification step.

---

# 64. Never Commit Credentials

Never place real values like:

```text
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
```

inside:

```text
main.tf
README.md
Git repository
Dockerfile
Jenkinsfile
screenshots
public tutorials
```

Treat credentials as secrets.

---

# 65. Return to Our Local Lab

Our first lab requires no AWS credentials.

Architecture:

```text
Local Machine
↓
Terraform CLI
↓
HashiCorp Local Provider
↓
Local File
```

This allows us to isolate Terraform mechanics.

---

# 66. Create `main.tf`

Inside:

```text
part-02-first-lab/
```

create:

```text
main.tf
```

Add:

```hcl
terraform {
  required_version = ">= 1.16.0, < 2.0.0"

  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "2.8.0"
    }
  }
}

resource "local_file" "welcome" {
  filename = "${path.module}/veriqta-terraform.txt"
  content  = "Terraform created this file.\nWelcome to the VERIQTA Terraform lab.\n"
}
```

Save the file.

---

# 67. Understand the Configuration Before Running It

Do not run copied Terraform without understanding it.

Start here:

```hcl
terraform {
}
```

This block contains Terraform-level settings.

---

# 68. `required_version`

We wrote:

```hcl
required_version = ">= 1.16.0, < 2.0.0"
```

This defines which Terraform CLI versions this configuration accepts.

It means:

```text
Terraform 1.16.0 or newer
but
not Terraform 2.0.0 or newer
```

This is not saying Terraform 2.0 currently exists.

It defines the compatibility boundary for this lab.

---

# 69. `required_providers`

We wrote:

```hcl
required_providers {
  local = {
    source  = "hashicorp/local"
    version = "2.8.0"
  }
}
```

This says the configuration requires the:

```text
hashicorp/local
```

provider at:

```text
2.8.0
```

For this reproducible lab, we intentionally select a specific provider version.

---

# 70. Provider Source Address

This:

```text
hashicorp/local
```

identifies the provider source.

Conceptually:

```text
registry.terraform.io/hashicorp/local
```

Terraform can use the Terraform Registry to locate the provider.

---

# 71. Why Use the Local Provider?

The Local provider manages local resources such as files.

That means our first infrastructure lifecycle can happen entirely on your machine.

No:

```text
AWS bill
IAM role
VPC
cloud account
```

is required.

But the Terraform workflow remains real.

---

# 72. Understand the Resource Block

We wrote:

```hcl
resource "local_file" "welcome" {
}
```

This creates a Terraform-managed resource.

Break it apart:

```text
resource
```

means:

```text
managed resource block
```

```text
local_file
```

is the resource type.

```text
welcome
```

is the local Terraform resource name.

---

# 73. Resource Address

Terraform can refer to this resource as:

```text
local_file.welcome
```

That is its resource address in this simple root module.

Remember this.

You will see resource addresses constantly in Terraform plans and state.

---

# 74. `filename`

We wrote:

```hcl
filename = "${path.module}/veriqta-terraform.txt"
```

`path.module` refers to the filesystem path of the module containing the expression.

For this root module, the file will be created in the project directory.

Result:

```text
part-02-first-lab/
└── veriqta-terraform.txt
```

---

# 75. `content`

We wrote:

```hcl
content = "Terraform created this file.\nWelcome to the VERIQTA Terraform lab.\n"
```

This is the content Terraform will place inside the managed file.

`\n` represents a newline.

Expected file:

```text
Terraform created this file.
Welcome to the VERIQTA Terraform lab.
```

---

# 76. Inspect the Project Before Initialization

Linux/macOS:

```bash
ls -la
```

PowerShell:

```powershell
Get-ChildItem -Force
```

You should have approximately:

```text
part-02-first-lab/
├── .git/
├── .gitignore
└── main.tf
```

You should **not** yet have:

```text
.terraform/
.terraform.lock.hcl
terraform.tfstate
veriqta-terraform.txt
```

That observation matters.

We are about to see which Terraform commands create which artifacts.

---

# 77. Run `terraform fmt`

Before initialization, run:

```bash
terraform fmt
```

Purpose:

```text
Format Terraform configuration
into Terraform's canonical style.
```

It may print:

```text
main.tf
```

if it reformatted the file.

Or it may print nothing if no changes were needed.

---

# 78. Verify Formatting

Open:

```text
main.tf
```

and inspect it.

You can also run:

```bash
terraform fmt -check
```

If formatting is acceptable, the command should exit successfully.

Later this becomes useful in CI/CD.

---

# 79. Try Validation Before Initialization

Now deliberately run:

```bash
terraform validate
```

Depending on the configuration and current working-directory state, Terraform should tell you initialization is required because the provider dependency has not yet been installed.

This is useful.

We deliberately encountered a failure.

---

# 80. Read the Error

Do not immediately search for a random fix.

Ask:

```text
What command failed?

What is Terraform telling me?

Which layer is missing?
```

We have configuration requiring:

```text
hashicorp/local
```

but the working directory has not been initialized.

The appropriate next step is:

```bash
terraform init
```

---

# 81. `terraform init`

Run:

```bash
terraform init
```

This initializes the Terraform working directory.

For our configuration, Terraform will:

```text
inspect provider requirements
↓
locate required provider
↓
download/install provider
↓
verify provider package
↓
create/update dependency lock file
↓
prepare .terraform directory
```

---

# 82. Expected Initialization Output

You should see output with sections similar to:

```text
Initializing the backend...

Initializing provider plugins...

Terraform has been successfully initialized!
```

Exact wording can differ by Terraform version.

You should also see Terraform locate/install the Local provider.

Read the output.

Do not train yourself to ignore command output.

---

# 83. What Changed?

List the directory again.

Linux/macOS:

```bash
ls -la
```

PowerShell:

```powershell
Get-ChildItem -Force
```

Now you should see:

```text
part-02-first-lab/
├── .git/
├── .terraform/
├── .terraform.lock.hcl
├── .gitignore
└── main.tf
```

Two important Terraform artifacts appeared:

```text
.terraform/
```

and:

```text
.terraform.lock.hcl
```

---

# 84. The `.terraform` Directory

Terraform automatically manages:

```text
.terraform/
```

The directory can contain local working-directory data such as:

```text
provider plugins
downloaded modules
backend-related metadata
workspace information
```

depending on the configuration.

For this lab, it contains the installed provider under Terraform's provider structure.

---

# 85. Inspect `.terraform`

Linux/macOS:

```bash
find .terraform -maxdepth 5 -type f
```

If your `find` implementation or depth differs, simply inspect with:

```bash
ls -R .terraform
```

PowerShell:

```powershell
Get-ChildItem .terraform -Recurse
```

Do not manually modify provider binaries.

Terraform manages this directory.

---

# 86. Should `.terraform/` Be Committed?

Normally:

```text
No.
```

That is why our `.gitignore` contains:

```gitignore
.terraform/
```

The directory can be regenerated through:

```bash
terraform init
```

The provider dependency selection is recorded separately in the lock file.

---

# 87. `.terraform.lock.hcl`

Initialization also created:

```text
.terraform.lock.hcl
```

This is the dependency lock file.

Open it.

You should see an entry for:

```text
registry.terraform.io/hashicorp/local
```

including information such as:

```text
version
constraints
hashes
```

Do not manually rewrite this file as normal workflow.

Terraform manages it.

---

# 88. Why the Lock File Exists

Your configuration says which provider versions are allowed or required.

The lock file records the selected provider dependency version and checksums.

This helps produce consistent future initialization behavior.

Conceptually:

```text
Configuration
↓
Allowed Provider Version
↓
terraform init
↓
Provider Selected
↓
Selection Recorded
↓
.terraform.lock.hcl
```

---

# 89. Should `.terraform.lock.hcl` Be Committed?

Yes, normally.

HashiCorp recommends committing the dependency lock file to version control.

That lets dependency changes participate in code review.

Our Git repository should therefore eventually include:

```text
main.tf
.gitignore
.terraform.lock.hcl
```

but not:

```text
.terraform/
```

---

# 90. Lock File vs `.terraform` Directory

Do not confuse them.

```text
.terraform/
```

is local working-directory data/cache used by Terraform.

```text
.terraform.lock.hcl
```

records dependency selections/checksums for the configuration.

Think:

```text
.terraform/
=
local generated working data
```

```text
.terraform.lock.hcl
=
version-controlled dependency lock information
```

---

# 91. Can `terraform init` Be Run Again?

Yes.

Run:

```bash
terraform init
```

again.

Terraform initialization is designed to be safe to repeat.

If nothing important changed, Terraform should largely confirm that the directory remains initialized.

You should not fear `terraform init`.

---

# 92. When Do You Re-run `terraform init`?

Common situations include changes to:

```text
provider requirements
module sources
module versions
backend configuration
```

Terraform may explicitly tell you reinitialization is required.

Read the error and follow the evidence.

---

# 93. Provider Installation

This is your first real provider lifecycle.

You wrote:

```hcl
required_providers {
  local = {
    source  = "hashicorp/local"
    version = "2.8.0"
  }
}
```

Then:

```bash
terraform init
```

performed the provider installation.

Architecture:

```text
main.tf
↓
Provider Requirement
↓
terraform init
↓
Terraform Registry
↓
Provider Package
↓
.terraform/
```

---

# 94. Terraform Core vs Provider

Terraform CLI itself did not need the ability to create a local file resource built directly into every Terraform installation.

Instead:

```text
Terraform Core
↓
Local Provider
↓
local_file resource
↓
Filesystem
```

This is the same provider architecture you will later use with AWS:

```text
Terraform Core
↓
AWS Provider
↓
AWS APIs
↓
AWS Infrastructure
```

---

# 95. Run `terraform validate`

Now run:

```bash
terraform validate
```

Expected result:

```text
Success! The configuration is valid.
```

Exact formatting may differ.

This tells us the configuration is syntactically valid and internally consistent within Terraform's validation scope.

---

# 96. What Validation Does Not Mean

Do not interpret:

```text
Success! The configuration is valid.
```

as:

```text
Every future operation will succeed.
```

Validation does not prove:

```text
cloud credentials work
IAM permissions are sufficient
API quotas are available
runtime services are healthy
business requirements are correct
```

Validation is one layer.

---

# 97. Deliberately Break Validation

Change:

```hcl
content = "Terraform created this file."
```

to an invalid configuration such as removing the closing quote:

```hcl
content = "Terraform created this file.
```

Save.

Run:

```bash
terraform validate
```

Terraform should report a syntax/configuration error.

Read it carefully.

---

# 98. Diagnose the Failure

Ask:

```text
Which file?

Which line?

What does Terraform expect?

What did I write?
```

Then restore:

```hcl
content = "Terraform created this file.\nWelcome to the VERIQTA Terraform lab.\n"
```

Run:

```bash
terraform fmt
terraform validate
```

Verification:

```text
configuration valid
```

You have just completed your first Terraform failure-and-recovery exercise.

---

# 99. Run `terraform plan`

Now:

```bash
terraform plan
```

Terraform evaluates:

```text
Configuration
+
Provider
+
Current State
+
Current Managed Resource Situation
↓
Proposed Changes
```

Because this is the first run, the resource does not exist in Terraform state yet.

Terraform should propose creating it.

---

# 100. Reading Terraform Plan Symbols

Terraform plan uses symbols to communicate actions.

For a resource to be created, you should see:

```text
+
```

and wording similar to:

```text
will be created
```

Near the end, expect a summary similar to:

```text
Plan: 1 to add, 0 to change, 0 to destroy.
```

Exact details may vary.

---

# 101. Read the Entire Resource Plan

Find:

```text
local_file.welcome
```

That is the resource address.

Terraform should show attributes associated with the resource.

Some values may be:

```text
known after apply
```

That means Terraform cannot know the final value until the operation occurs.

This is normal.

---

# 102. What Has `plan` Created?

Important question:

Did:

```bash
terraform plan
```

create:

```text
veriqta-terraform.txt
```

No.

Verify.

Linux/macOS:

```bash
ls -la
```

PowerShell:

```powershell
Get-ChildItem -Force
```

The target file should not yet exist.

This teaches:

```text
Plan
≠
Apply
```

---

# 103. Plan Is a Proposal

Think:

```text
terraform plan
=
Here is what Terraform proposes to change.
```

It is your opportunity to inspect:

```text
creation
updates
replacement
destruction
unexpected values
```

before changing managed infrastructure.

---

# 104. Run `terraform apply`

Now run:

```bash
terraform apply
```

Terraform will calculate/show the proposed actions and request approval in an interactive local workflow.

Read the plan.

Do not immediately type approval.

Confirm:

```text
1 to add
0 to change
0 to destroy
```

Then enter:

```text
yes
```

when prompted.

---

# 105. Expected Apply Result

Terraform should create the resource.

Near the end, expect something similar to:

```text
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

Again, exact output can vary.

Now verify.

---

# 106. Verify the Managed Resource

Linux/macOS:

```bash
cat veriqta-terraform.txt
```

PowerShell:

```powershell
Get-Content .\veriqta-terraform.txt
```

Expected content:

```text
Terraform created this file.
Welcome to the VERIQTA Terraform lab.
```

We now have:

```text
Terraform Configuration
↓
Terraform CLI
↓
Local Provider
↓
Real Managed File
```

---

# 107. Inspect the Directory Again

You should now have approximately:

```text
part-02-first-lab/
├── .git/
├── .terraform/
├── .terraform.lock.hcl
├── .gitignore
├── main.tf
├── terraform.tfstate
└── veriqta-terraform.txt
```

A new critical artifact appeared:

```text
terraform.tfstate
```

---

# 108. State Has Arrived

Terraform now needs to track the managed resource.

Conceptually:

```text
main.tf
↓
Desired Resource

terraform.tfstate
↓
Terraform's tracked managed-resource information

veriqta-terraform.txt
↓
Real Resource
```

Do not manually edit:

```text
terraform.tfstate
```

Part 7 is dedicated to state.

---

# 109. Inspect State Safely

Instead of manually editing the state file, ask Terraform what resources it tracks:

```bash
terraform state list
```

Expected:

```text
local_file.welcome
```

Then:

```bash
terraform state show local_file.welcome
```

Terraform displays stored information about the managed resource.

---

# 110. First State Mental Model

You now have three important layers:

```text
main.tf
↓
What you want

terraform.tfstate
↓
What Terraform tracks

veriqta-terraform.txt
↓
Actual managed object
```

This is the foundation of Terraform lifecycle management.

---

# 111. Run Plan Again

Without changing anything:

```bash
terraform plan
```

What should happen?

Terraform should normally report no required changes.

Conceptually:

```text
Desired
=
Managed Reality
↓
No Change
```

This demonstrates repeatability.

---

# 112. Why Terraform Does Not Create Another File

You did not write:

```text
Run this creation command every time.
```

You declared:

```text
This resource should exist with this configuration.
```

Terraform tracks it.

That is declarative lifecycle management.

---

# 113. Change the Desired State

Modify:

```hcl
content = "Terraform created this file.\nWelcome to the VERIQTA Terraform lab.\n"
```

to:

```hcl
content = "Terraform manages infrastructure as code.\nThis file has now been updated by Terraform.\n"
```

Save.

Run:

```bash
terraform fmt
terraform validate
terraform plan
```

---

# 114. Read the Change Plan

Terraform should detect that the desired content changed.

Do not apply yet.

Find the difference.

Terraform's plan output should show the old/new values or otherwise indicate the resource action required by this provider/resource.

The exact action semantics are provider-specific.

The lesson is:

```text
Configuration Changed
↓
Terraform Detected Difference
↓
Plan Explains Proposed Action
```

---

# 115. Apply the Change

After reviewing:

```bash
terraform apply
```

Review again.

Approve:

```text
yes
```

Then verify:

Linux/macOS:

```bash
cat veriqta-terraform.txt
```

PowerShell:

```powershell
Get-Content .\veriqta-terraform.txt
```

Expected:

```text
Terraform manages infrastructure as code.
This file has now been updated by Terraform.
```

---

# 116. You Have Now Managed Change

Your workflow was:

```text
Initial Desired State
↓
Apply
↓
Resource Exists
↓
Change Configuration
↓
Plan Again
↓
Apply Again
↓
Resource Updated
```

This is the lifecycle from Part 1 becoming real.

---

# 117. Deliberately Create Drift

Now we are going to break the system.

Do **not** modify `main.tf`.

Instead, manually modify:

```text
veriqta-terraform.txt
```

Change its content to:

```text
I changed this file manually outside Terraform.
```

Save.

Now:

```text
Terraform Configuration
≠
Real Resource
```

This is an example of drift.

---

# 118. Detect the Drift

Run:

```bash
terraform plan
```

Read what Terraform reports.

Terraform should observe that the managed local file no longer matches the declared configuration and propose the provider-appropriate action needed to return it to the desired state.

Do not memorize the exact action.

Understand the principle:

```text
Manual Change
↓
Terraform Observes Difference
↓
Plan Reports Proposed Reconciliation
```

---

# 119. Reconcile the Drift

Run:

```bash
terraform apply
```

Review.

Approve.

Then inspect the file again.

Terraform should return it to the declared content:

```text
Terraform manages infrastructure as code.
This file has now been updated by Terraform.
```

You have now experienced drift and reconciliation.

---

# 120. Terraform Output Is Evidence

From now on, do not think of Terraform output as terminal noise.

Output tells you things such as:

```text
which provider is being installed
which version was selected
which resource is changing
what action is proposed
which values changed
whether initialization succeeded
whether validation succeeded
whether apply succeeded
```

Read it.

---

# 121. Common Terraform Action Symbols

You will commonly encounter plan indicators representing actions such as:

```text
+       create
-       destroy
~       update in place
-/+     destroy and then create replacement
+/-     create replacement then destroy old
```

Exact presentation can evolve.

Always read Terraform's legend in the plan output rather than relying only on memory.

---

# 122. `known after apply`

You may see:

```text
(known after apply)
```

This means Terraform cannot determine that final value during planning.

The provider/API operation must occur first.

Examples can include generated identifiers or computed attributes.

This is not automatically an error.

---

# 123. `terraform destroy`

Now complete the resource lifecycle.

Run:

```bash
terraform destroy
```

Terraform should produce a destruction plan.

Read it.

Expected summary should indicate approximately:

```text
0 to add, 0 to change, 1 to destroy
```

Do not approve blindly.

Confirm the resource:

```text
local_file.welcome
```

is the resource being removed.

Then enter:

```text
yes
```

---

# 124. Verify Destruction

Linux/macOS:

```bash
ls -la
```

PowerShell:

```powershell
Get-ChildItem -Force
```

The file:

```text
veriqta-terraform.txt
```

should no longer exist.

Now check Terraform state:

```bash
terraform state list
```

The managed resource should no longer appear.

---

# 125. What Destroy Does Not Remove

Notice that `terraform destroy` does not mean:

```text
delete my Terraform project.
```

You should still have:

```text
main.tf
.terraform/
.terraform.lock.hcl
terraform.tfstate
.gitignore
.git/
```

Terraform destroyed the managed resource.

It did not delete your configuration.

---

# 126. Configuration vs Infrastructure

After destroy:

```text
Configuration:
local_file should exist
```

but:

```text
Current managed infrastructure:
resource absent
```

If you run:

```bash
terraform plan
```

again, Terraform should propose creating the resource again.

This proves an important concept:

```text
Destroying Infrastructure
≠
Deleting Desired Configuration
```

---

# 127. Recreate the Resource

Run:

```bash
terraform plan
```

You should again see:

```text
1 to add
```

Then:

```bash
terraform apply
```

Approve after review.

Verify:

```bash
terraform state list
```

and inspect the file.

You have now demonstrated reproducibility.

---

# 128. Git Status

Run:

```bash
git status
```

Because of `.gitignore`, you should not see `.terraform/` or state files proposed for normal Git tracking.

You should see files such as:

```text
.gitignore
main.tf
.terraform.lock.hcl
```

as untracked if they have not yet been committed.

---

# 129. First Commit

Stage the intended repository files:

```bash
git add main.tf .gitignore .terraform.lock.hcl
```

Inspect:

```bash
git status
```

Then commit:

```bash
git commit -m "Add first Terraform lab"
```

You have now combined:

```text
Infrastructure as Code
+
Dependency Locking
+
Version Control
```

---

# 130. What Should Be in Git?

For this lab:

```text
COMMIT

main.tf
.gitignore
.terraform.lock.hcl
```

Normally do not commit:

```text
.terraform/
terraform.tfstate
terraform.tfstate.*
```

The generated local file is also a lab resource rather than source code.

Whether generated artifacts belong in Git depends on their purpose, but this Terraform-managed lab output does not need to be committed.

---

# 131. Common Failure: `terraform: command not found`

Symptom:

```text
terraform: command not found
```

Possible causes:

```text
Terraform not installed
wrong binary downloaded
binary not extracted
directory not in PATH
terminal not restarted
installation created multiple versions
```

Investigate:

Linux/macOS:

```bash
which terraform
echo "$PATH"
```

Windows:

```powershell
Get-Command terraform
$env:Path
```

Fix the installation/PATH problem.

Verify:

```bash
terraform version
```

---

# 132. Common Failure: Wrong Terraform Version

Symptom:

You installed a new Terraform version but:

```bash
terraform version
```

shows another version.

Possible cause:

```text
multiple Terraform executables exist
```

Investigate:

Linux/macOS:

```bash
which terraform
```

Windows:

```powershell
Get-Command terraform -All
```

Your PATH order determines which executable may be selected.

Do not repeatedly reinstall Terraform without finding which executable is actually running.

---

# 133. Common Failure: Wrong CPU Architecture

Symptoms may include execution-format or architecture-related errors.

Investigate:

```bash
uname -m
```

Then confirm the downloaded Terraform package matches your operating system and architecture.

Example:

```text
Linux AMD64 package
≠
Linux ARM64 package
```

---

# 134. Common Failure: Permission Denied

You may have a Terraform binary that exists but cannot execute.

On Unix-like systems, inspect:

```bash
ls -l /path/to/terraform
```

A manually installed binary may require correct executable permissions.

Do not randomly run everything with:

```bash
sudo
```

Understand the actual permissions problem first.

---

# 135. Common Failure: Provider Download Failure

During:

```bash
terraform init
```

Terraform may fail while locating or downloading a provider.

Possible causes include:

```text
no internet connection
DNS failure
proxy configuration
firewall restriction
registry unavailable
invalid provider source
invalid version constraint
TLS/certificate problems
corporate network restrictions
```

Investigation:

```text
1. Read the exact error.
2. Confirm internet connectivity.
3. Confirm provider source.
4. Confirm provider version.
5. Check Terraform Registry access.
6. Check proxy/firewall restrictions.
7. Retry only after understanding the likely cause.
```

---

# 136. Do Not Solve Provider Failures by Downloading Random Binaries

Providers are executable plugins.

Treat them as software supply-chain dependencies.

Do not respond to a provider installation error by downloading an arbitrary binary from an unknown website.

Use trusted provider distribution mechanisms.

---

# 137. Common Failure: Invalid Provider Version

Suppose your configuration requests a provider version that does not exist.

`terraform init` cannot satisfy that requirement.

The solution is not:

```text
keep running init
```

Investigate the provider's available releases and your version constraint.

---

# 138. Common Failure: Lock File Conflict

You may eventually change provider constraints while the lock file still records an older selected version.

Terraform may tell you the selections are inconsistent or that initialization is required.

Do not delete the lock file automatically.

Understand:

```text
configured constraints
vs
locked provider selection
```

When intentionally upgrading within allowed constraints, Terraform supports:

```bash
terraform init -upgrade
```

We will handle dependency upgrades properly later.

---

# 139. Common Failure: Running Terraform from the Wrong Directory

Symptom:

```text
No configuration files
```

or Terraform appears to operate on the wrong project.

Check:

Linux/macOS:

```bash
pwd
ls -la
```

PowerShell:

```powershell
Get-Location
Get-ChildItem -Force
```

Confirm:

```text
Am I inside the intended Terraform root module?
```

---

# 140. Common Failure: Configuration Syntax Error

Symptom:

Terraform points to a `.tf` file and line.

Investigation:

```text
Read file
Read line
Read error
Check quotes
Check braces
Check block structure
Check argument syntax
```

Then:

```bash
terraform fmt
terraform validate
```

Do not troubleshoot AWS when HCL cannot even parse.

---

# 141. Common Failure: AWS Authentication

This does not affect our Local provider lab, but you will encounter it later.

Symptoms may include errors indicating:

```text
credentials unavailable
expired credentials
invalid token
invalid access key
```

Investigation should include:

```bash
aws sts get-caller-identity
```

If using a named profile:

```bash
aws sts get-caller-identity --profile your-profile-name
```

If using IAM Identity Center and the session expired:

```bash
aws sso login --profile your-profile-name
```

Then verify again.

---

# 142. Common Failure: AWS Authorization

Suppose:

```bash
aws sts get-caller-identity
```

works.

But Terraform receives:

```text
AccessDenied
```

for a resource operation.

That suggests:

```text
Authentication succeeded
↓
Authorization failed
```

Investigate the IAM permissions required for the requested operation.

Do not rotate credentials randomly when the error is actually permission-related.

---

# 143. Common Failure: Wrong AWS Account

This is a serious operational risk.

Before cloud infrastructure operations, verify:

```bash
aws sts get-caller-identity
```

Confirm the expected:

```text
account
identity/role context
```

Also verify your intended AWS Region.

Do not assume your terminal is using the account you used yesterday.

---

# 144. Common Failure: Wrong AWS Profile

If:

```text
AWS_PROFILE
```

is set, tooling may use that profile.

Linux/macOS:

```bash
echo "$AWS_PROFILE"
```

PowerShell:

```powershell
$env:AWS_PROFILE
```

Then verify:

```bash
aws sts get-caller-identity
```

Never debug cloud infrastructure without first knowing which identity you are using.

---

# 145. Common Failure: Environment Variable Overrides

AWS environment variables can override values from profiles.

You may think:

```text
profile A is active
```

while an environment variable causes different credentials or configuration to be selected.

Troubleshooting therefore includes checking the environment.

Never print secret environment-variable values into screenshots, tickets, public chat, CI logs, or documentation.

---

# 146. Evidence-First Troubleshooting Model

Use this sequence:

```text
Symptom
↓
Exact Error
↓
Current Directory
↓
Terraform Version
↓
Configuration
↓
Initialization
↓
Provider
↓
State
↓
Credentials
↓
Authorization
↓
External API
↓
Managed Resource
↓
Root Cause
↓
Fix
↓
Verify
```

Do not use:

```text
Error
↓
Random command from internet
↓
Another error
↓
sudo everything
```

---

# 147. Failure Lab: Delete `.terraform`

Make sure your managed local file exists first.

Now delete only:

```text
.terraform/
```

Do **not** delete:

```text
main.tf
.terraform.lock.hcl
terraform.tfstate
```

Then try:

```bash
terraform plan
```

Terraform should indicate that initialization/provider installation is required.

What did we learn?

```text
.terraform/
contains local initialization artifacts needed by the working directory.
```

---

# 148. Recover from Missing `.terraform`

Run:

```bash
terraform init
```

Terraform should reinstall the required provider using the configuration and lock information.

Then:

```bash
terraform validate
terraform plan
```

The project is operational again.

This demonstrates why:

```text
.terraform/
```

does not need to be committed to Git.

It can be regenerated.

---

# 149. Failure Lab: Delete the Managed File

Ensure Terraform has created:

```text
veriqta-terraform.txt
```

Delete that file manually.

Do not change Terraform configuration.

Run:

```bash
terraform plan
```

Terraform should detect that the managed resource is missing and propose restoring it.

Apply after review:

```bash
terraform apply
```

Verify the file returns.

---

# 150. Failure Lab: Break `main.tf`

Remove a closing brace.

Run:

```bash
terraform validate
```

Read the error.

Restore the brace.

Then:

```bash
terraform fmt
terraform validate
```

Verification:

```text
configuration valid
```

---

# 151. Failure Lab: Wrong Provider Version

Temporarily change:

```hcl
version = "2.8.0"
```

to an intentionally impossible version such as:

```hcl
version = "99.99.99"
```

Run:

```bash
terraform init -upgrade
```

Terraform should fail because it cannot satisfy the provider requirement.

Read the error.

Restore:

```hcl
version = "2.8.0"
```

Then:

```bash
terraform init
```

Verify success.

This demonstrates:

```text
Provider constraints
must match
real available provider versions.
```

---

# 152. First Complete Lab Architecture

You have now built:

```text
LOCAL MACHINE
│
├── Git Repository
│
├── VS Code
│
├── Terraform CLI
│
└── Terraform Working Directory
     │
     ├── main.tf
     │
     ├── .terraform.lock.hcl
     │
     ├── .terraform/
     │
     └── terraform.tfstate
              │
              ▼
        Terraform Core
              │
              ▼
       HashiCorp Local Provider
              │
              ▼
       Local Filesystem
              │
              ▼
     veriqta-terraform.txt
```

That is a real Terraform-managed system.

Small, but complete.

---

# 153. Map Every File to Its Purpose

## `main.tf`

```text
Desired Terraform configuration
```

## `.terraform/`

```text
Generated local Terraform working data,
including installed providers/modules as applicable
```

## `.terraform.lock.hcl`

```text
Locked provider dependency selections and checksums
```

## `terraform.tfstate`

```text
Local Terraform state
```

## `.gitignore`

```text
Prevents inappropriate generated/sensitive local files
from being accidentally committed
```

## `veriqta-terraform.txt`

```text
The real resource managed by Terraform
```

---

# 154. Map Every Command to Its Purpose

## Version

```bash
terraform version
```

Purpose:

```text
Show Terraform version/platform information.
```

## Help

```bash
terraform -help
```

Purpose:

```text
Show CLI help and commands.
```

## Format

```bash
terraform fmt
```

Purpose:

```text
Format Terraform configuration.
```

## Initialize

```bash
terraform init
```

Purpose:

```text
Prepare working directory,
providers,
modules,
and backend-related initialization.
```

## Validate

```bash
terraform validate
```

Purpose:

```text
Check configuration syntax and internal consistency.
```

## Plan

```bash
terraform plan
```

Purpose:

```text
Calculate and display proposed changes.
```

## Apply

```bash
terraform apply
```

Purpose:

```text
Execute approved changes.
```

## Destroy

```bash
terraform destroy
```

Purpose:

```text
Plan and perform destruction of managed resources.
```

---

# 155. Command Order

For a new project:

```text
Write
↓
terraform fmt
↓
terraform init
↓
terraform validate
↓
terraform plan
↓
terraform apply
↓
Verify
```

You will sometimes see `init` before `fmt`.

That is fine.

Formatting does not require provider installation.

For this course, the important operational rule is:

```text
Initialize before provider-dependent operations.
```

---

# 156. Our Standard Engineering Workflow

As the series progresses, our workflow becomes:

```text
Understand Requirement
↓
Design
↓
Write
↓
Format
↓
Initialize
↓
Validate
↓
Test
↓
Plan
↓
Review
↓
Apply
↓
Verify
↓
Monitor
```

Terraform is not merely:

```text
terraform apply
```

---

# 157. Verification Matters

After:

```bash
terraform apply
```

we did not stop at:

```text
Apply complete!
```

We checked the actual resource.

For the local lab:

```bash
cat veriqta-terraform.txt
```

Later with AWS, verification may include:

```text
AWS CLI
HTTP request
DNS lookup
health endpoint
AWS Console
CloudWatch
network test
```

Successful Terraform execution and successful service operation are different questions.

---

# 158. Cleanup

If you want to finish the lab with no managed resource:

```bash
terraform destroy
```

Review.

Approve.

Verify the file is gone.

Then:

```bash
terraform state list
```

should show no managed resources.

---

# 159. Optional Local Workspace Cleanup

After destroying the resource, you may delete generated local Terraform working artifacts if you intentionally want a completely clean local checkout:

```text
.terraform/
terraform.tfstate
terraform.tfstate.backup
```

Do not delete:

```text
main.tf
.gitignore
.terraform.lock.hcl
.git/
```

if you want to preserve the project.

Running:

```bash
terraform init
```

will recreate `.terraform/`.

A future apply will create new state as resources are managed again.

---

# 160. Do Not Confuse Cleanup with Production State Management

Deleting:

```text
terraform.tfstate
```

in this disposable local lab after all resources are destroyed is one thing.

Deleting production Terraform state is completely different and can be disastrous.

Later we will use protected remote state.

Never generalize this beginner cleanup into:

```text
state files are safe to delete.
```

They are not.

---

# 161. Knowledge Check

Answer without looking back.

1. What is Terraform CLI?

2. What is PATH?

3. Why can Terraform be installed but still return `command not found`?

4. How do you verify the Terraform version?

5. How do you display Terraform help?

6. What is a Terraform working directory?

7. What file extension normally contains Terraform configuration?

8. Does Terraform execute `.tf` files sequentially by filename?

9. What does `terraform init` do?

10. What is `.terraform/`?

11. Should `.terraform/` normally be committed?

12. What is `.terraform.lock.hcl`?

13. Should `.terraform.lock.hcl` normally be committed?

14. What does `terraform fmt` do?

15. What does `terraform validate` prove?

16. What does it not prove?

17. What does `terraform plan` do?

18. Does plan normally perform the proposed resource changes?

19. What does `terraform apply` do?

20. Why must you read the plan before approving?

21. What does `terraform destroy` do?

22. Does destroy delete your `.tf` configuration?

23. What is Terraform state?

24. Why did our first lab use the Local provider?

25. What did `local_file.welcome` represent?

26. What happened when the managed file was changed manually?

27. What is drift?

28. What happened when `.terraform/` was deleted?

29. How did we recover it?

30. Why do provider versions matter?

31. What is AWS CLI?

32. Does Terraform require AWS CLI to manage every provider?

33. What is authentication?

34. What is authorization?

35. What command can verify the current AWS caller identity?

36. Why should root credentials not be used for normal Terraform work?

37. Why should AWS credentials not be hardcoded in `.tf` files?

38. What is `AWS_PROFILE`?

39. Why can environment variables cause confusing authentication behavior?

40. What is the complete first-lab workflow?

---

# 162. Knowledge Check Answers

1. The command-line program used to run Terraform operations.

2. An environment variable containing directories the shell searches for executable programs.

3. The Terraform executable's directory may not be in PATH, or the current shell may not have refreshed its environment.

4.

```bash
terraform version
```

5.

```bash
terraform -help
```

6. The directory containing the Terraform root-module configuration being operated on.

7.

```text
.tf
```

8. No. Terraform evaluates the module configuration as a whole and determines relationships.

9. It initializes the working directory, including providers, modules, and backend-related setup as required.

10. Terraform-managed local working-directory data/cache.

11. Normally no.

12. Terraform's dependency lock file for selected provider versions/checksums.

13. Normally yes.

14. Formats Terraform configuration into canonical style.

15. That Terraform can validate the configuration's syntax and internal consistency within its validation scope.

16. It does not prove cloud authentication, authorization, runtime health, quotas, or successful future deployment.

17. Calculates and displays proposed infrastructure changes.

18. No.

19. Executes approved infrastructure changes.

20. Because the plan may contain unexpected, destructive, expensive, or insecure changes.

21. Plans and performs destruction of Terraform-managed resources.

22. No.

23. Terraform's stored information about its managed-resource bindings and related attributes.

24. So we could learn Terraform's lifecycle without AWS credentials, permissions, networking, or cost.

25. The Terraform resource address for our managed local file.

26. Terraform detected the difference during planning and proposed reconciliation.

27. A difference between intended managed configuration and the real managed resource.

28. Terraform could no longer use the locally installed provider from that initialized working directory.

29.

```bash
terraform init
```

30. Provider releases can change schemas, capabilities, behavior, fixes, and compatibility.

31. Amazon Web Services' command-line interface.

32. No. Terraform providers communicate with their corresponding APIs. AWS CLI is a separate tool useful for AWS interaction and verification.

33. Establishing who the caller is.

34. Determining what that caller may do.

35.

```bash
aws sts get-caller-identity
```

36. The root user has extremely powerful account-level access and should not be the normal automation identity.

37. Credentials are secrets and can leak through Git, logs, copies, screenshots, and collaboration systems.

38. An environment variable commonly used to select a named AWS profile.

39. Environment variables can override or influence profile-based configuration and cause tools to use an identity/configuration different from what you expected.

40.

```text
Create Directory
↓
Write Configuration
↓
terraform init
↓
terraform fmt
↓
terraform validate
↓
terraform plan
↓
Review
↓
terraform apply
↓
Verify
↓
Change
↓
Plan Again
↓
Apply Again
↓
Verify
↓
terraform destroy
↓
Verify Destruction
```

---

# 163. Part 2 Cheat Sheet

## Check Terraform

```bash
terraform version
```

## Terraform Help

```bash
terraform -help
```

## Command Help

```bash
terraform plan -help
```

## Format

```bash
terraform fmt
```

## Check Formatting

```bash
terraform fmt -check
```

## Initialize

```bash
terraform init
```

## Validate

```bash
terraform validate
```

## Plan

```bash
terraform plan
```

## Apply

```bash
terraform apply
```

## Destroy

```bash
terraform destroy
```

## List Managed Resources

```bash
terraform state list
```

## Inspect a Managed Resource in State

```bash
terraform state show local_file.welcome
```

## Check AWS CLI

```bash
aws --version
```

## Verify AWS Caller

```bash
aws sts get-caller-identity
```

## AWS IAM Identity Center Login

```bash
aws sso login --profile your-profile-name
```

---

# 164. Files to Remember

```text
*.tf
=
Terraform configuration
```

```text
.terraform/
=
generated working-directory data
```

```text
.terraform.lock.hcl
=
provider dependency lock file
```

```text
terraform.tfstate
=
local state when using the local backend
```

```text
.gitignore
=
Git exclusion rules
```

---

# 165. First Lab Mental Model

You started with:

```text
Empty Directory
```

Then:

```text
main.tf
```

declared:

```text
Desired Resource
```

Then:

```bash
terraform init
```

created/prepared:

```text
.terraform/
.terraform.lock.hcl
provider installation
```

Then:

```bash
terraform plan
```

showed:

```text
what Terraform intended to do
```

Then:

```bash
terraform apply
```

produced:

```text
terraform.tfstate
+
veriqta-terraform.txt
```

Then a configuration change produced:

```text
New Desired State
↓
New Plan
↓
New Apply
↓
Updated Resource
```

Then a manual resource change produced:

```text
Drift
↓
Plan
↓
Reconciliation
```

Finally:

```bash
terraform destroy
```

removed the managed resource.

---

# 166. Final Architecture

You should now understand this architecture from actual experience:

```text
                         LOCAL MACHINE
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
            Git             VS Code       Terraform CLI
                                                  │
                                                  ▼
                                       Terraform Configuration
                                              main.tf
                                                  │
                                                  ▼
                                          Terraform Core
                                             /        \
                                            /          \
                                           ▼            ▼
                                        State       Lock File
                                           \            /
                                            \          /
                                             ▼        ▼
                                          Local Provider
                                               │
                                               ▼
                                        Local Filesystem
                                               │
                                               ▼
                                  veriqta-terraform.txt
```

Later we will replace:

```text
Local Provider
↓
Local Filesystem
```

with architectures such as:

```text
AWS Provider
↓
AWS API
↓
VPC
↓
Subnet
↓
Security Group
↓
EC2
```

The Terraform lifecycle remains recognizable.

---

# 167. Part 2 Completion Checklist

Do not move forward until you can do these yourself.

```text
[ ] Open a terminal

[ ] Check your current directory

[ ] Verify Terraform installation

[ ] Explain PATH

[ ] Locate the Terraform executable

[ ] Use terraform -help

[ ] Create a Terraform project directory

[ ] Create a .tf configuration

[ ] Explain what a provider requirement means

[ ] Run terraform fmt

[ ] Run terraform init

[ ] Explain what .terraform/ contains

[ ] Explain .terraform.lock.hcl

[ ] Explain why the lock file belongs in Git

[ ] Run terraform validate

[ ] Deliberately break and fix configuration

[ ] Run terraform plan

[ ] Read the plan

[ ] Identify a resource address

[ ] Run terraform apply

[ ] Verify the actual resource

[ ] Inspect Terraform state

[ ] Change desired configuration

[ ] Plan the change

[ ] Apply the change

[ ] Create manual drift

[ ] Detect the drift

[ ] Reconcile the drift

[ ] Run terraform destroy

[ ] Verify destruction

[ ] Recreate the resource

[ ] Use Git to version the configuration

[ ] Explain AWS CLI's purpose

[ ] Explain authentication vs authorization

[ ] Explain why credentials must not be hardcoded
```

---

# 168. Part 2 Completion Standard

You have completed Part 2 when you can start with:

```text
Empty Machine / Development Environment
```

and understand how to reach:

```text
Terraform Installed
↓
Terraform CLI Verified
↓
Project Directory Created
↓
Configuration Written
↓
Provider Declared
↓
Working Directory Initialized
↓
Provider Installed
↓
Dependency Locked
↓
Configuration Validated
↓
Plan Reviewed
↓
Resource Applied
↓
Resource Verified
↓
State Inspected
↓
Configuration Changed
↓
Change Planned
↓
Change Applied
↓
Drift Created
↓
Drift Detected
↓
Drift Reconciled
↓
Resource Destroyed
↓
Destruction Verified
```

More importantly, if something fails, you should no longer immediately think:

```text
Terraform is broken.
```

You should ask:

```text
Is Terraform installed?

Is PATH correct?

Am I in the correct directory?

Is the configuration valid?

Has the directory been initialized?

Was the provider installed?

Does the lock file match the requirements?

Is state present?

Is authentication available?

Is authorization sufficient?

Can Terraform reach the provider registry/API?

What does the exact error say?
```

That is the beginning of real Terraform troubleshooting.

---

# 169. What Comes Next

You now know how to operate Terraform.

But our `main.tf` is still simple.

You have seen syntax such as:

```hcl
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "2.8.0"
    }
  }
}

resource "local_file" "welcome" {
  filename = "${path.module}/veriqta-terraform.txt"
  content  = "Terraform manages infrastructure as code.\n"
}
```

In Part 2, you learned how to run it.

In the next part, you need to understand exactly how to **read and write Terraform configuration yourself**.

That means:

```text
blocks
arguments
attributes
expressions
strings
numbers
booleans
null
lists
sets
maps
objects
tuples
references
conditionals
for expressions
splat expressions
type constraints
type conversion
unknown values
sensitive values
```

That leads directly to:

```text
Part 3:
HCL and Terraform Configuration Language
```

---

# Official Resources

HashiCorp Terraform Installation

https://developer.hashicorp.com/terraform/install

Terraform CLI Documentation

https://developer.hashicorp.com/terraform/cli

Terraform CLI Commands

https://developer.hashicorp.com/terraform/cli/commands

Terraform `init`

https://developer.hashicorp.com/terraform/cli/commands/init

Terraform Working Directory Initialization

https://developer.hashicorp.com/terraform/cli/init

Terraform `fmt`

https://developer.hashicorp.com/terraform/cli/commands/fmt

Terraform `validate`

https://developer.hashicorp.com/terraform/cli/commands/validate

Terraform `plan`

https://developer.hashicorp.com/terraform/cli/commands/plan

Terraform `apply`

https://developer.hashicorp.com/terraform/cli/commands/apply

Terraform `destroy`

https://developer.hashicorp.com/terraform/cli/commands/destroy

Terraform Dependency Lock File

https://developer.hashicorp.com/terraform/language/files/dependency-lock

Terraform Provider Requirements

https://developer.hashicorp.com/terraform/language/providers/requirements

HashiCorp Local Provider

https://registry.terraform.io/providers/hashicorp/local/latest

Terraform Registry

https://registry.terraform.io/

HashiCorp Terraform VS Code Extension

https://marketplace.visualstudio.com/items?itemName=HashiCorp.terraform

Visual Studio Code

https://code.visualstudio.com/

Git

https://git-scm.com/

AWS CLI Installation

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

AWS CLI Configuration

https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

AWS CLI Environment Variables

https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html

AWS IAM Identity Center with AWS CLI

https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html

AWS STS GetCallerIdentity

https://docs.aws.amazon.com/cli/latest/reference/sts/get-caller-identity.html

